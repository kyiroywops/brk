from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('estudiantes', views.estudiantes, name="estudiantes"),
    path('asignaturas', views.asignaturas, name="asignaturas"),
    path('enrolamiento', views.enrolamiento, name="enrolamiento"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)