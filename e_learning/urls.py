from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('', views.StudentList.as_view(), name="index"),
    path('detail/<slug:pk>', views.StudentDetail.as_view(), name="detail"),
    path('add_student', views.StudentCreate.as_view(), name="add_student"),
    path('edit_student/<slug:pk>', views.StudentUpdate.as_view(), name="edit_student"),
    path('delete_student/<slug:pk>', views.StudentDelete.as_view(), name="delete_student"),


    path('api/all', views.get_all_students_api, name="all_students_api"),
    path('api/add', views.add_student_api, name="add_student_api"),
    path('api/student/<int:id>', views.one_student, name="student_api"),
]
