from django.urls import path
from . import views

#URL Configuration

urlpatterns = [
    path('',views.welcome_page),

    
    path('update_menu',views.update_menu),
    path('update_banci',views.update_banci),
    path('update_clienti',views.update_clienti),
    path('update_imprumuturi',views.update_imprumuturi),


    path('create_menu', views.create_menu),
    path('create_banci',views.create_banci),
    path('create_clienti',views.create_clienti),
    path('create_imprumuturi',views.create_imprumuturi),
    
    
    path('update_banca/<int:banca_id>/', views.update_banci, name='update_banci'),
    path('update_clienti/<int:client_id>/', views.update_clienti, name='update_clienti'),
    path('update_imprumut/<int:imprumuturi_id>/', views.update_imprumuturi, name='update_imprumuturi'),
    


    path('delete_banca/<int:banca_id>/', views.delete_banci, name='delete_banci'),
    path('delete_clienti/<int:client_id>/', views.delete_clienti, name='delete_clienti'),
    path('delete_imprumuturi/<int:imprumut_id>/', views.delete_imprumuturi, name='delete_imprumuturi')
    



    ]