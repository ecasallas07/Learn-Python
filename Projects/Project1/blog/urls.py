from django.urls import path
# with the point call all files
from . import views

urlpatterns = [
    path("",views.index, name="index")
]
