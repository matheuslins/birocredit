from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include(('core.urls', 'core'), namespace='core')),
    path('pessoas/', include(('pessoa.urls', 'pessoa'), namespace='pessoa')),
    path('admin/', admin.site.urls),
]
