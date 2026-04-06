from django.urls import path
from .views import RoleView, UserView

urlpatterns = [
    path('roles/', RoleView.as_view(), name='roles'),
    path('users/', UserView.as_view(), name='users'),
]