from django.urls import path, include
from . import views

urlpatterns = [
    path('api/', views.WomenApiView.as_view(), name='api')
]




