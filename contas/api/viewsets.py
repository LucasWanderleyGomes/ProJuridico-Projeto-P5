from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
# from .serializer import SignUpSerializer
from .serializer import CreateUserSerializer
from contas.models import User

class SignUpView(viewsets.ModelViewSet):

    """
    Endpoint de criação de usuários (signup).
    Utiliza `Djoser` com extensão para validação de e-mail único.
    
    """
     
    queryset = User.objects.all()  
    # serializer_class = SignUpSerializer
    serializer_class = CreateUserSerializer

    def create(self, request: Request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "aviso": "Usuário criado com sucesso",
                "dados": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# from .serializer import SignUpSerializer
# from contas.models import User
# from rest_framework import generics, status, viewsets
# from rest_framework.response import Response
# from rest_framework.request import Request


# class SignUpView(generics.GenericAPIView):
#     serializer_class = SignUpSerializer

#     def post(self, request:Request):
#         data = request.data
#         serializer = self.serializer_class(data=data)

#         if serializer.is_valid():
#             serializer.save()
            

#             response={
#                 "message":"Usuário criado com sucesso",
#                 "data": serializer.data
#             }

#             return Response(data=response, status=status.HTTP_201_CREATED)
        
#         return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)