from django.urls import path
from .views import ListCards

urlpatterns = [
    path('',ListCards.as_view())
]