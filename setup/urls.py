
from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet)
router.register('cursos', CursosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
