from django.urls import re_path

from .views import PessoaDetalheView, EventosDetalheView


urlpatterns = [
    re_path(
        r'^(?P<cpf>\d+)/$',
        PessoaDetalheView.as_view(),
        name='pessoa-detalhe'
    ),
    re_path(
        r'^(?P<cpf>\d+)/eventos/$',
        EventosDetalheView.as_view(),
        name='eventos-detalhe'
    ),
]
