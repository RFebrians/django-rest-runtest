from django.urls import path, include
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'birthdays', views.BirthdayViewSet)

urlpatterns = [
    path('todos/<int:pk>/', views.delTodo),
    path('todos/', views.TodoList),
    path('passwords/', views.PasswordList),
    path('birthdays/', views.BirthdayList),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
]
