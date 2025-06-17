from django.urls import path
from . import views

urlpatterns = [
    path('get_ipl/',views.get_ipl ,name="get_ipl"),
    path('post_ipl/',views.post_ipl,name="post_ipl"),
    path('put_ipl/<int:id>/',views.put_ipl,name="put_ipl"),
    path('delete_ipl/<int:id>/',views.delete_ipl,name="delete_ipl"),
    path('get_student/',views.get_student,name="get_student"),
    path('get_students/<int:id>/',views.get_students,name="get_students"),
]