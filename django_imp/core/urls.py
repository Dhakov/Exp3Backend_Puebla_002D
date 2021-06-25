from django.urls import path
from .views import form_software, index, software

urlpatterns = [
    path('', index, name="index"),
    path('', software, name="software"),
    path('form_software', form_software, name = "form_software"),
]