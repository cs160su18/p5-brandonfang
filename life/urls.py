from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.index, name='index'),
    path('', views.login, name='login'),
    path('groups/', views.groups, name='groups'),
    path('lists/', views.lists, name='lists'),
#     path('users/', views.users, name='users'),
    # path('activity/',views.activity, name='activity'),
]
