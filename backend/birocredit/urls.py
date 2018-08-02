from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('scores/', include(('score.urls', 'score'), namespace='score')),
    path('pessoas/', include(('pessoa.urls', 'pessoa'), namespace='pessoa')),
    path('admin/', admin.site.urls),
]
