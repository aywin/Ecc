from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.custom_login, name='login'),
    path('index/', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('addrec/', views.addrec, name='addrec'),
    path('update/uprec/<int:id>/', views.uprec, name='uprec'),
    path ('delete/<int:id>/', views.delete,name='delete'),
    path ('update/<int:id>/', views.update,name='update'),
    # Définissez d'autres URLs pour d'autres vues de votre application si nécessaire
]
