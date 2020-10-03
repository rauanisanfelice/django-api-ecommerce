from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import Produto, Categoria


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Produto
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Categoria
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = '__all__'