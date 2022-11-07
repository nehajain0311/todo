
from django.urls import path
from .views import index,delete,update,add,detail, TaskListView, TaskDetailView, TaskUpdateView,TaskDeleteView,TaskCreateView

app_name="todoapp"

urlpatterns = [
    path("",index,name="index"),
    path("update/<int:id>/",update,name="update"),
    path("delete/<int:task_id>/",delete,name="delete"),    
    path("add/",add,name="add"),
    path("detail/<int:task_id>/",detail,name="detail"),
    path("cbvindex/",TaskListView.as_view(),name="cbvindex"),
    path("cbvadd/",TaskCreateView.as_view(),name="cbvadd"),
    path("cbvdetail/<int:pk>/",TaskDetailView.as_view(),name="cbvdetail"),
    path("cbvupdate/<int:pk>/",TaskUpdateView.as_view(),name="cbvupdate"),
    path("cbvdelete/<int:pk>/",TaskDeleteView.as_view(),name="cbvdelete"),
]