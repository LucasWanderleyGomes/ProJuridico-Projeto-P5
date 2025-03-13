from rest_framework import generics
from .models import Processo
from processo.api.serializers import ProcessoSerializer

# Create your views here.
class ProcessosAPIView(generics.ListCreateAPIView):
    queryset = Processo.objects.all()
    serializer_class = ProcessoSerializer

class ProcessoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Processo.objects.all()
    serializer_class = ProcessoSerializer