
from django.urls import path
from .views import index,delete,add

app_name="todoapp"

urlpatterns = [
    path("",index,name="index"),
    path("add/",add,name="add"),
    path("delete/<int:task_id>/",delete,name="delete"),
    
]