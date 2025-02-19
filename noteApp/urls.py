from django.contrib import admin
from django.urls import path, include
from note import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('note/', include('note.urls')),  
    path('accounts/', include('django.contrib.auth.urls')),  
    path('', views.base_view, name='base'),
]