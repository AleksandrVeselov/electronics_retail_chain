from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from employee.apps import EmployeeConfig

app_name = EmployeeConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='employee/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]