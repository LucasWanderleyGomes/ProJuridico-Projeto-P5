from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from processo.models import Processo

class ProcessoModelTest(TestCase):
    def setUp(self):
        self.processo = Processo.objects.create(
            categoria="Trabalhista",
            titulo="Processo de rescisão",
            descricao="Processo referente a rescisão contratual"
        )
    
    def test_processo_creation(self):
        """Testa a criação de um processo"""
        self.assertEqual(self.processo.titulo, "Processo de rescisão")
        self.assertEqual(self.processo.categoria, "Trabalhista")
        self.assertTrue(self.processo.ativo)
        self.assertIsNotNone(self.processo.data_criacao)
        self.assertIsNotNone(self.processo.criacao)
        
    def test_str_representation(self):
        """Testa a representação string do modelo"""
        self.assertEqual(str(self.processo), "Processo de rescisão")


class ProcessoViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.list_url = '/api/v2/processos/'  # URL direta sem usar reverse com namespace
        
        self.processo1 = Processo.objects.create(
            categoria="Trabalhista",
            titulo="Processo 1",
            descricao="Descrição 1"
        )
        self.processo2 = Processo.objects.create(
            categoria="Civil",
            titulo="Processo 2",
            descricao="Descrição 2"
        )
    
    def test_get_all_processos(self):
        """Testa listagem de todos os processos"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)  # Considerando a paginação
        
    def test_get_single_processo(self):
        """Testa obtenção de um processo específico"""
        detail_url = f'{self.list_url}{self.processo1.pk}/'
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['titulo'], self.processo1.titulo)
        
    def test_create_processo(self):
        """Testa criação de um novo processo"""
        data = {
            'categoria': 'Criminal',
            'titulo': 'Novo Processo',
            'descricao': 'Descrição do novo processo'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Processo.objects.count(), 3)
        
    def test_update_processo(self):
        """Testa atualização de um processo"""
        detail_url = f'{self.list_url}{self.processo1.pk}/'
        data = {
            'titulo': 'Título Atualizado',
            'descricao': 'Descrição Atualizada',
            'categoria': 'Trabalhista'
        }
        response = self.client.put(detail_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.processo1.refresh_from_db()
        self.assertEqual(self.processo1.titulo, 'Título Atualizado')
        
    def test_delete_processo(self):
        """Testa exclusão de um processo"""
        detail_url = f'{self.list_url}{self.processo1.pk}/'
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Processo.objects.count(), 1)
        
    def test_pagination(self):
        """Testa se a paginação está funcionando"""
        # Criando mais processos para testar paginação
        for i in range(3, 8):
            Processo.objects.create(
                categoria=f"Categoria {i}",
                titulo=f"Processo {i}",
                descricao=f"Descrição {i}"
            )
        
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 5)  # page_size definido como 5
        self.assertIn('next', response.data)  # Verifica se tem próxima página