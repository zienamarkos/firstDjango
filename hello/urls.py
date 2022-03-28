from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("zena", views.zena, name="zena"),
    path("<str:name>", views.greet, name="greet")
]
