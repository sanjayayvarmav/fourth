
from django.urls import path, include

from todoapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.TaskList.as_view(),name='cbvhome'),
    path('cbvdetails/<int:pk>/',views.TaskDetail.as_view(),name='cbvdetails'),
    path('cbvupdates/<int:pk>/',views.TaskUpdate.as_view(),name='cbvupdates'),
    path('cbvdelete/<int:pk>/',views.Taskdelete.as_view(),name='cbvdelete'),
]