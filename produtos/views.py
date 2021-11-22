from rest_framework.decorators import permission_classes
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import DjangoModelPermissions, BasePermission, IsAuthenticated, SAFE_METHODS

from .models import Fornecedor, Produto
from .serializers import FornecedorSerializer, ProdutoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .permissions import EhSuperUser

class FornercedortList(APIView, LimitOffsetPagination):
    """
    List all fornecedores, or create a new fornecedor.
    """
    permission_classes = (permissions.DjangoModelPermissions, )
    queryset = Fornecedor.objects.all()
    default_limit = 1

    def get(self, request, format=None):
        fornecedores = Fornecedor.objects.all()
        results = self.paginate_queryset(fornecedores, request, view=self)
        serializer = FornecedorSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        fornecedor = FornecedorSerializer(data=request.data)
        if fornecedor.is_valid():
            fornecedor.save()
            return Response(fornecedor.data, status=status.HTTP_201_CREATED)
        return Response(fornecedor.errors, status=status.HTTP_400_BAD_REQUEST)


class FornecedorDetail(APIView):
    """
    Retrieve, update or delete a fornecedor instance.
    """
    """permission_classes = (
        EhSuperUser, # permissão personalizada onde só admins podem deletar Fornecedores
        permissions.DjangoModelPermissions,)"""

    queryset = Fornecedor.objects.all()

    def get_object(self, pk):
        try:
            return Fornecedor.objects.get(pk=pk)
        except Fornecedor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        fornecedor = self.get_object(pk)
        serializer = FornecedorSerializer(fornecedor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        fornecedor = self.get_object(pk)
        serializer = FornecedorSerializer(fornecedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(FornecedorSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        fornecedor = self.get_object(pk)
        fornecedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FornecedorDetailParticular(APIView):
    """
    Endpoint personalisado
    """
    def pegarFornecedor(self, pk):
        return Fornecedor.objects.get(pk=pk)

    def get(self, request, pk, format=None):

        try:
            fornecedor = self.pegarFornecedor(pk)
            serializer = FornecedorSerializer(fornecedor)
            return Response(serializer.data)
        except Fornecedor.DoesNotExist:
            return Response("Fornecedor não foi encontrado", status=status.HTTP_404_NOT_FOUND)


class ProdutoList(APIView):
    """
    List all produtos, or create a new produto.
    """
    def get(self, request, format=None):
        snippets = Produto.objects.all()
        serializer = ProdutoSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProdutoDetail(APIView):
    """
    Retrieve, update or delete a produto instance.
    """
    def get_object(self, pk):
        try:
            return Produto.objects.get(pk=pk)
        except Produto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        produto = self.get_object(pk)
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        produto = self.get_object(pk)
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(ProdutoSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        produto = self.get_object(pk)
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
