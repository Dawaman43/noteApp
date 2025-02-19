from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_view, name='base'),
    path('notes/', views.notes, name='note'),
    path('view_notes/', views.note_view, name='view_note'),
    path('edit_note/<int:pk>/', views.edit_note, name='edit_note'),
    path('delete_note/<int:pk>/', views.delete_note, name='delete_note'),
    path('categories/', views.category_list, name='category_list'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/<int:pk>/', views.edit_category, name='edit_category'),
    path('delete_category/<int:pk>/', views.delete_category, name='delete_category'),
]