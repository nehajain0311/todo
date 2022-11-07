
from django.urls import path
from .views import index,delete,add,update

app_name="todoapp"

urlpatterns = [
    path("",index,name="index"),
    path("update/<int:id>/",update,name="update"),
    path("delete/<int:task_id>/",delete,name="delete"),
    
]