from django.urls import path, include
from . import views

urlpatterns = [
    path('luke_skywalker/', views.get_luke_info),
    path('X-wing/', views.get_X_wing),
    path('Imperial_shuttle/', views.get_Imperial_shuttle),
    path('lave_1/', views.get_Slave_1)
]