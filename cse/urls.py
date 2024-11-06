from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('1/', views.student_list, name='student_list')

]
