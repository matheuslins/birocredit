from django.urls import path, include
from .views import PessoaDetalheView, EventosDetalheView


urlpatterns = [
    path(
        '<int>',
        PessoaDetalheView.as_view(),
        name='pessoa-detalhe'
    ),
    path(
        '<int>/eventos',
        EventosDetalheView.as_view(),
        name='eventos-detalhe'
    ),
]
