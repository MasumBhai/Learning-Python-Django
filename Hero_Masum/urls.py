from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("<int:id>",views.index,name="index"),
   # path("<int:id>",views.anything,name="anything"),
   # path("<int:id>",views.urlError,name="urlError"),
]