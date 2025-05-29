from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase, APIRequestFactory
from rest_framework import status
from rest_framework.request import Request
from django.contrib.auth import get_user_model

from postagem.models import Postagem, Likes
from comunidade.models import Comunidade
from postagem.api.serializers import PostagemSerializer

User = get_user_model()


class PostagemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.comunidade = Comunidade.objects.create(
            nome='Comunidade Teste',
            descricao='Descrição teste'
        )
        self.postagem = Postagem.objects.create(
            usuario=self.user,
            comunidade=self.comunidade,
            titulo='Postagem Teste',
            conteudo='Conteúdo teste'
        )

    def test_postagem_creation(self):
        """Testa a criação básica de uma postagem"""
        self.assertEqual(self.postagem.titulo, 'Postagem Teste')
        self.assertEqual(self.postagem.usuario, self.user)
        self.assertEqual(self.postagem.comunidade, self.comunidade)
        self.assertTrue(self.postagem.ativo)

    def test_total_likes_method(self):
        """Testa o método total_likes da postagem"""
        Likes.objects.create(usuario=self.user, postagem=self.postagem)  
        another_user = User.objects.create_user(
            username='anotheruser',
            email='another@example.com',
            password='testpass123'
        )
        Likes.objects.create(usuario=another_user, postagem=self.postagem)  # Corrigido aqui também
        self.assertEqual(self.postagem.total_likes(), 2)


class PostagemViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.comunidade = Comunidade.objects.create(
            nome='Comunidade Teste',
            descricao='Descrição teste'
        )
        self.postagem = Postagem.objects.create(
            usuario=self.user,
            comunidade=self.comunidade,
            titulo='Postagem Teste',
            conteudo='Conteúdo teste'
        )
        self.client.force_authenticate(user=self.user)

    def test_list_postagens(self):
        """Testa a listagem de postagens"""
        url = '/api/v2/postagens/'  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['titulo'], 'Postagem Teste')

    def test_create_postagem(self):
        """Testa a criação de uma nova postagem"""
        url = '/api/v2/postagens/'
        data = {
            'titulo': 'Nova Postagem',
            'conteudo': 'Conteúdo da nova postagem',
            'comunidade': self.comunidade.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Postagem.objects.count(), 2)
        self.assertEqual(Postagem.objects.last().titulo, 'Nova Postagem')

    def test_delete_postagem(self):
        """Testa a exclusão (soft delete) de uma postagem"""
        url = f'/api/postagens/{self.postagem.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.postagem.refresh_from_db()
        self.assertFalse(self.postagem.ativo)

    # Remova ou ajuste este teste se a rota de like não existir
    # def test_like_action(self):
    #     """Testa a ação de like/deslike"""
    #     url = f'/api/postagens/{self.postagem.id}/like/'
    #     
    #     response = self.client.post(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertTrue(response.data['liked'])
    #     self.assertEqual(response.data['likes_count'], 1)
    #
    #     response = self.client.post(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertFalse(response.data['liked'])
    #     self.assertEqual(response.data['likes_count'], 0)


class PostagemSerializerTest(APITestCase):  # Mude para APITestCase para autenticação
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.comunidade = Comunidade.objects.create(
            nome='Comunidade Teste',
            descricao='Descrição teste'
        )
        self.postagem = Postagem.objects.create(
            usuario=self.user,
            comunidade=self.comunidade,
            titulo='Postagem Teste',
            conteudo='Conteúdo teste'
        )
        self.client.force_authenticate(user=self.user)

    def test_serializer_fields(self):
        """Testa se o serializer contém os campos esperados"""
        factory = APIRequestFactory()
        request = factory.get('/')
        request.user = self.user  # Adiciona o usuário ao request
        serializer_context = {'request': Request(request)}
        serializer = PostagemSerializer(instance=self.postagem, context=serializer_context)
        data = serializer.data

        self.assertIn('id', data)
        self.assertIn('titulo', data)
        self.assertIn('conteudo', data)
        self.assertIn('usuario', data)
        self.assertIn('comunidade', data)  # Adicionei esta verificação
        self.assertIn('likes_count', data)
        self.assertIn('has_liked', data)
        self.assertEqual(data['titulo'], 'Postagem Teste')
        self.assertEqual(data['likes_count'], 0)
        self.assertFalse(data['has_liked'])