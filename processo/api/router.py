from .viewsets import ProcessoViewSet
from rest_framework.routers import SimpleRouter

processoRouter = SimpleRouter()
processoRouter.register('processos', ProcessoViewSet)