from django.urls import re_path
from .views import (ScoreDetalheView, EnderecoListCreateView,
                    BensListCreateView)


urlpatterns = [
    re_path(
        r'^scores/(?P<cpf>\d+)/$',
        ScoreDetalheView.as_view(),
        name='score-detalhe'
    ),
    re_path(
        r'^endereco/$',
        EnderecoListCreateView.as_view(),
        name='endereco-create'
    ),
    re_path(
        r'^bens/$',
        BensListCreateView.as_view(),
        name='bem-create'
    ),
]
