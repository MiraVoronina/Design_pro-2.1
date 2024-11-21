from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Домашняя страница
    path('login/', views.login_user, name='login'),  # Страница авторизации
    path('register/', views.register, name='register'),  # Страница регистрации
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
