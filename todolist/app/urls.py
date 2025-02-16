from django.urls import path
from . import views
urlpatterns = [
    path('', views.To_do_list, name='list_name'),
    path('home/', views.home, name='home_name'),
    path('contact/<int:pk>/', views.contact, name='contact_name'),
    path('edit/<int:pk>/', views.edit, name='edit_name'),
    path('history/', views.history, name='history_name'),
    path('history/delete/<int:pk>/', views.history_delete, name='history_delete'),  # Delete task URL
]