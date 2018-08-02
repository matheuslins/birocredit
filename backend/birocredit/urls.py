from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include(('core.urls', 'core'), namespace='core')),
    path('admin/', admin.site.urls),
]
