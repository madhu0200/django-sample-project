from django.urls import path
from . import views
from typing_extensions import Required
urlpatterns=[
    path('home/',views.home),
    path('submit/',views.submit),
    path('registration/',views.register)
]