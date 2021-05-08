from django.urls import path
from .views import ListPasswords

urlpatterns = [
    path('',ListPasswords.as_view())
]