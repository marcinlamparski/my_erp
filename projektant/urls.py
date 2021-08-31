from django.urls import path
from . import views



urlpatterns = [
    path('projektowanie/', views.projektowanie),
    path('projekty/', views.projekty),
    path('marszruty/', views.marszruty),

]