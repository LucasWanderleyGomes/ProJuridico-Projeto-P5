from .viewsets import SignUpView
from rest_framework.routers import SimpleRouter

user_router = SimpleRouter()
user_router.register('signup', SignUpView, basename='signup')