from django.urls import path
from .views import FornercedortList, FornecedorDetail, ProdutoList, ProdutoDetail, FornecedorDetailParticular

urlpatterns = [
    path('fornecedores/', FornercedortList.as_view()),
    path('fornecedores/<int:pk>/', FornecedorDetail.as_view()),
    path('fornecedores/particular/<int:pk>/', FornecedorDetailParticular.as_view()),

    path('produtos/', ProdutoList.as_view()),
    path('produtos/<int:pk>/', ProdutoDetail.as_view()),
]
