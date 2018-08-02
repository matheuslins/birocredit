from django.urls import path, include
from .views import ScoreDetalheView


urlpatterns = [
    path(
        '<int>',
        ScoreDetalheView.as_view(),
        name='score-detalhe'
    )
]
