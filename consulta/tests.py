from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from consulta.models import Consulta
from contas.models import User
from django.utils import timezone
from consulta.api.serializers import ConsultaSerializer
import json

class ConsultaModelTest(TestCase):
    def setUp(self):
        """Configuração inicial para os testes de modelo"""
        self.consulta = Consulta.objects.create(
            nome_cliente="Cliente Teste",
            numero_processo="12345",
            assunto="Assunto Teste",
            descricao="Descrição da consulta teste"
        )

    def test_consulta_creation(self):
        """Testa se uma consulta é criada corretamente"""
        self.assertEqual(self.consulta.nome_cliente, "Cliente Teste")
        self.assertEqual(self.consulta.numero_processo, "12345")
        self.assertEqual(self.consulta.assunto, "Assunto Teste")
        self.assertEqual(self.consulta.descricao, "Descrição da consulta teste")
        self.assertTrue(self.consulta.ativo)
        self.assertIsNotNone(self.consulta.criacao)
        self.assertIsNotNone(self.consulta.atualizacao)

    def test_verbose_names(self):
        """Testa os nomes amigáveis no Meta do modelo"""
        self.assertEqual(Consulta._meta.verbose_name, "Consulta")
        self.assertEqual(Consulta._meta.verbose_name_plural, "Consultas")

    def test_ordering(self):
        """Testa a ordenação padrão definida no Meta"""
        self.assertEqual(Consulta._meta.ordering, ['criacao'])

    def test_str_representation(self):
        """Testa a representação em string do modelo"""
        expected_str = f"Consulta {self.consulta.id} - Cliente: Cliente Teste | Processo: 12345"
        self.assertEqual(str(self.consulta), expected_str)


class ConsultaSerializerTest(TestCase):
    def setUp(self):
        """Configuração inicial para os testes de serializer"""
        self.consulta_data = {
            'nome_cliente': 'Cliente Serializer',
            'numero_processo': '54321',
            'assunto': 'Assunto Serializer',
            'descricao': 'Testando o serializer'
        }
        self.serializer = ConsultaSerializer(data=self.consulta_data)

    def test_contains_expected_fields(self):
        """Testa se o serializer contém todos os campos esperados"""
        data = ConsultaSerializer(instance=Consulta.objects.create(
            nome_cliente="Test",
            numero_processo="1",
            assunto="Test"
        )).data
        expected_fields = {
            'id', 'nome_cliente', 'assunto', 'descricao', 
            'numero_processo', 'criacao', 'atualizacao', 'ativo'
        }
        self.assertEqual(set(data.keys()), expected_fields)

    def test_valid_data(self):
        """Testa o serializer com dados válidos"""
        self.assertTrue(self.serializer.is_valid())

    def test_read_only_fields(self):
        """Testa se os campos read-only estão configurados corretamente"""
        read_only_fields = {'criacao', 'atualizacao'}
        serializer = ConsultaSerializer()
        for field in read_only_fields:
            self.assertTrue(field in serializer.fields)
            self.assertTrue(serializer.fields[field].read_only)


class ConsultaViewSetTest(APITestCase):
    def setUp(self):
        """Configuração inicial para os testes de API"""
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
            username='testuser'
        )
        self.client.force_authenticate(user=self.user)
        
        # Cria duas consultas para testes
        self.consulta1 = Consulta.objects.create(
            nome_cliente="Cliente 1",
            numero_processo="11111",
            assunto="Assunto 1",
            descricao="Descrição 1"
        )
        self.consulta2 = Consulta.objects.create(
            nome_cliente="Cliente 2",
            numero_processo="22222",
            assunto="Assunto 2",
            descricao="Descrição 2"
        )
        
        # Payloads para testes de criação/atualização
        self.valid_payload = {
            'nome_cliente': 'Novo Cliente',
            'numero_processo': '33333',
            'assunto': 'Novo Assunto',
            'descricao': 'Nova Descrição'
        }
        self.invalid_payload = {
            'nome_cliente': '',  # Inválido porque é required
            'numero_processo': '44444',
            'assunto': 'Assunto Inválido',
            'descricao': 'Descrição Inválida'
        }

    def test_get_all_consultas(self):
        """Testa listar todas as consultas"""
        response = self.client.get(reverse('consulta-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_get_valid_single_consulta(self):
        """Testa obter uma consulta específica"""
        response = self.client.get(
            reverse('consulta-detail', kwargs={'pk': self.consulta1.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome_cliente'], self.consulta1.nome_cliente)

    def test_get_invalid_single_consulta(self):
        """Testa obter uma consulta que não existe"""
        response = self.client.get(
            reverse('consulta-detail', kwargs={'pk': 999})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_consulta(self):
        """Testa criar uma nova consulta com dados válidos"""
        response = self.client.post(
            reverse('consulta-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_consulta(self):
        """Testa criar uma nova consulta com dados inválidos"""
        response = self.client.post(
            reverse('consulta-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_consulta(self):
        """Testa atualizar uma consulta existente"""
        response = self.client.put(
            reverse('consulta-detail', kwargs={'pk': self.consulta1.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_consulta(self):
        """Testa deletar uma consulta existente"""
        response = self.client.delete(
            reverse('consulta-detail', kwargs={'pk': self.consulta1.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_consulta_ordering(self):
        """Testa se as consultas são ordenadas por data de criação (mais antigas primeiro)"""
        # Cria uma nova consulta que deve aparecer por último
        nova_consulta = Consulta.objects.create(
            nome_cliente="Novo Cliente",
            numero_processo="99999",
            assunto="Novo Assunto"
        )
        
        response = self.client.get(reverse('consulta-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verifica a ordenação pelos IDs (o mais antigo vem primeiro)
        results = response.data['results'] if 'results' in response.data else response.data
        self.assertEqual(results[0]['id'], self.consulta1.id)  # Mais antigo
        self.assertEqual(results[1]['id'], self.consulta2.id)   # Do meio
        self.assertEqual(results[2]['id'], nova_consulta.id)    # Mais novo