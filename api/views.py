import logging

from django.contrib.auth.models import User

from rest_framework import mixins, generics, permissions, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.schemas.openapi import AutoSchema

from .models import Produto, Categoria
from .serializers import ProdutoSerializer, CategoriaSerializer, UserSerializer

logger = logging.getLogger(__name__)


class UserList(generics.ListAPIView):
    """Lista todos usuários."""

    schema = AutoSchema(tags=["Usuários"])

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def dispatch(self, request, *args, **kwargs):
        logger.info(f"UserList {request.method} ({request.user.username})")
        return super().dispatch(request, *args, **kwargs)


class UserDetail(generics.RetrieveAPIView):
    """Detalhes do usuário."""

    schema = AutoSchema(tags=["Usuários"])

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def dispatch(self, request, *args, **kwargs):
        logger.info(f"UserDetail {request.method} ({request.user.username})")
        return super().dispatch(request, *args, **kwargs)


class ProdutoList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """Lista todos produtos, ou cria um novo produto."""

    schema = AutoSchema(tags=["Produtos"])

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def dispatch(self, request, *args, **kwargs):
        logger.info(f"ProdutoList {request.method} ({request.user.username})")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProdutoDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    
    schema = AutoSchema(tags=["Produtos"])

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def dispatch(self, request, *args, **kwargs):
        logger.info(f"ProdutoDetail {request.method} ({request.user.username})")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CategoriaList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """Lista todas categorias, ou cria uma nova categoria."""

    schema = AutoSchema(tags=["Categorias"])

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def dispatch(self, request, *args, **kwargs):
        logger.info(f"CategoriaList {request.method} ({request.user.username})")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoriaDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    
    schema = AutoSchema(tags=["Categorias"])
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def dispatch(self, request, *args, **kwargs):
        logger.info(f"CategoriaDetail {request.method} ({request.user.username})")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)