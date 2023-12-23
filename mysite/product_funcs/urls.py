from django.urls import path
from .views import base_view

app_name = 'product_funcs'  # This is the namespace for your app's URLs

urlpatterns = [
    path('base/', base_view, name='base'),
]