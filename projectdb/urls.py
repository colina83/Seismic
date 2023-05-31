from django.urls import path,include
from .views import login,home


urlpatterns = [
    path('',login,name='login'),
    path('home/',home,name='home'),
]
