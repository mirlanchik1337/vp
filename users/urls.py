from django.urls import path
from .views import LoginViewSet, RegisterViewSet
create_list = {'get': 'list', 'post': 'post'}

urlpatterns = [
    path('login/', LoginViewSet.as_view(create_list)),
    path('register/', RegisterViewSet.as_view(create_list))
]