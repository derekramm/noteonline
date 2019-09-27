from django.urls import path, include

from note import views

app_name = 'note'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('create/', views.create, name='create'),
    path('detail/<int:id>', views.detail, name='detail'),
]
