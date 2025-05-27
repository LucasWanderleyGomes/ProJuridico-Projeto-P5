from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from comunidade.models import Comunidade
from postagem.models import Postagem
from blog.models import BlogPosts
from contas.models import User  # Import your custom User model
from comunidade.api.serializers import ComunidadeSerializer
import json

class ComunidadeModelTest(TestCase):
    def setUp(self):
        self.comunidade = Comunidade.objects.create(
            nome="Comunidade Teste",
            descricao="Descrição da comunidade teste",
            regras="Regras da comunidade teste"
        )

    def test_comunidade_creation(self):
        """Test if comunidade is created correctly"""
        self.assertEqual(self.comunidade.nome, "Comunidade Teste")
        self.assertEqual(self.comunidade.descricao, "Descrição da comunidade teste")
        self.assertEqual(self.comunidade.regras, "Regras da comunidade teste")
        self.assertIsNotNone(self.comunidade.data_criacao)

    def test_verbose_names(self):
        """Test verbose names in Meta class"""
        self.assertEqual(Comunidade._meta.verbose_name, "Comunidade")
        self.assertEqual(Comunidade._meta.verbose_name_plural, "Comunidades")

    def test_ordering(self):
        """Test ordering in Meta class"""
        self.assertEqual(Comunidade._meta.ordering, ['id'])

    def test_str_representation(self):
        """Test string representation of comunidade"""
        self.assertEqual(str(self.comunidade), "Comunidade Teste")


class ComunidadeSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
            username='testuser'
        )
        self.comunidade = Comunidade.objects.create(
            nome="Comunidade Serializer",
            descricao="Testando o serializer",
            regras="Regras para teste"
        )
        
        self.serializer_data = {
            'nome': 'Nova Comunidade',
            'descricao': 'Descrição nova',
            'regras': 'Novas regras'
        }
        self.serializer = ComunidadeSerializer(instance=self.comunidade)

    def test_contains_expected_fields(self):
        """Test if serializer contains all expected fields"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), 
                         {'id', 'nome', 'descricao', 'regras', 'data_criacao', 'postagens', 'blogPosts'})

    def test_field_content(self):
        """Test content of serializer fields"""
        data = self.serializer.data
        self.assertEqual(data['nome'], self.comunidade.nome)
        self.assertEqual(data['descricao'], self.comunidade.descricao)
        self.assertEqual(data['regras'], self.comunidade.regras)
        

    def test_create_comunidade(self):
        """Test creating a new comunidade through serializer"""
        serializer = ComunidadeSerializer(data=self.serializer_data)
        self.assertTrue(serializer.is_valid())
        comunidade = serializer.save()
        self.assertEqual(comunidade.nome, self.serializer_data['nome'])
        self.assertEqual(comunidade.descricao, self.serializer_data['descricao'])
        self.assertEqual(comunidade.regras, self.serializer_data['regras'])


class ComunidadeViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
            username='testuser'
        )
        self.client.force_authenticate(user=self.user)
        
        self.comunidade1 = Comunidade.objects.create(
            nome="Comunidade 1",
            descricao="Descrição 1",
            regras="Regras 1"
        )
        self.comunidade2 = Comunidade.objects.create(
            nome="Comunidade 2",
            descricao="Descrição 2",
            regras="Regras 2"
        )
        
        
        self.valid_payload = {
            'nome': 'Nova Comunidade',
            'descricao': 'Nova Descrição',
            'regras': 'Novas Regras'
        }
        self.invalid_payload = {
            'nome': '',
            'descricao': 'Descrição inválida',
            'regras': 'Regras inválidas'
        }

    def test_get_all_comunidades(self):
        """Test retrieving all comunidades"""
        response = self.client.get(reverse('comunidade-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_get_valid_single_comunidade(self):
        """Test retrieving a single comunidade"""
        response = self.client.get(
            reverse('comunidade-detail', kwargs={'pk': self.comunidade1.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], self.comunidade1.nome)

    def test_get_invalid_single_comunidade(self):
        """Test retrieving a non-existent comunidade"""
        response = self.client.get(
            reverse('comunidade-detail', kwargs={'pk': 999})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_comunidade(self):
        """Test creating a new comunidade with valid data"""
        response = self.client.post(
            reverse('comunidade-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_comunidade(self):
        """Test creating a new comunidade with invalid data"""
        response = self.client.post(
            reverse('comunidade-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_comunidade(self):
        """Test updating an existing comunidade"""
        response = self.client.put(
            reverse('comunidade-detail', kwargs={'pk': self.comunidade1.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_comunidade(self):
        """Test deleting an existing comunidade"""
        response = self.client.delete(
            reverse('comunidade-detail', kwargs={'pk': self.comunidade1.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_authentication_required(self):
        """Test that authentication is required for all operations"""
        self.client.logout()
        
        # Test list
        response = self.client.get(reverse('comunidade-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        # Test create
        response = self.client.post(
            reverse('comunidade-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        # Test retrieve
        response = self.client.get(
            reverse('comunidade-detail', kwargs={'pk': self.comunidade1.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)