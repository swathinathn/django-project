from django.urls import path
from . import views

urlpatterns =[
    path('students/', views.get_students),
    path('students/create/',views.create_student),
    path('students/update/<int:id>', views.update_student),
    path("students/delete/<int:id>/", views.delete_student),
    path('student_form/', views.students_create, name='student_create'),

   path('register/', views.register, name='register'),
   path('login/', views.user_login, name='login'),
   path('logout/', views.user_logout, name='logout'),
   path('home/', views.home, name='home'),
   path('staff/', views.staff_page, name='staff'),
   path('adminn/', views.admin_page,name='adminn')
]