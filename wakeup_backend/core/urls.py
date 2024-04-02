from django.urls import path

from core import views

urlpatterns = [
    path('me/', views.me, name='me'),
    path('get-my-pc/', views.get_my_pc, name='get_my_pc'),
    path('wake-up/', views.wake_up_computer, name='wake_up'),    
]