from django.contrib import admin
from django.urls import path

from api.views import home, get_sum

urlpatterns = [
    path('home/', home),
    path('get-sum/', get_sum),
]
