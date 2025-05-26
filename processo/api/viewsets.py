from rest_framework import generics, viewsets
from processo.models import Processo
from processo.api.serializers import ProcessoSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.


# ============================== API VERSÃO 1  (V1) ==============================
# class ProcessosAPIView(generics.ListCreateAPIView):
#     queryset = Processo.objects.all()
#     serializer_class = ProcessoSerializer

# class ProcessoAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Processo.objects.all()
#     serializer_class = ProcessoSerializer

# ============================== API VERSÃO 2  (V2) ==============================
from rest_framework.pagination import PageNumberPagination
class ProcessoPagination(PageNumberPagination):
    page_size = 5

class ProcessoViewSet(viewsets.ModelViewSet):
    queryset = Processo.objects.all()
    serializer_class = ProcessoSerializer
    pagination_class = ProcessoPagination



    

   