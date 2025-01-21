from django.urls import path, re_path
from . import views

app_name = "users"

urlpatterns = [
    path('', views.users_list, name='users_list'),  # List all users
    path('<int:id>/', views.user_detail, name='user_detail'),  # User details by ID
    path('redirect/', views.user_detail_redirect, name='user_detail_redirect'),  # Redirect for search
    re_path(r'^filter/even/$', views.filter_even_users, name='filter_even_users'),  # Regex-based route for even user IDs
]
