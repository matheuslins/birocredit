from django.urls import re_path
from .views import ScoreDetalheView


urlpatterns = [
    re_path(
        r'^scores/(?P<cpf>\d+)/$',
        ScoreDetalheView.as_view(),
        name='score-detalhe'
    )
]
