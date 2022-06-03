from django.urls import path
from articles import views

urlpatterns = [
    path('index/', views.index),
    path('dinner/<str:name>', views.dinner),
    path('review/', views.review),
    path('create_review/', views.create_review),
]
