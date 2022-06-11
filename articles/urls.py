from django.urls import path
from articles import views


app_name = 'articles'
urlpatterns = [
    path('index/', views.index),
    path('dinner/', views.dinner, name='dinner'),
    path('review/', views.review, name='review'),
    path('create_review/', views.create_review, name='create_review'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),

]
