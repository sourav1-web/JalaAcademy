
from django.urls import path,include
from testapp import views

urlpatterns = [
    path('',views.HomeView),
    path('Insert_Employee/',views.InsertEmployee,name='Insert_Employee'),
    path('List_Employee/',views.ListEmployee,name='List_Employee'),
    path('update/<int:id>/', views.UpdateEmployee, name='update_employee'),
    path('delete/<int:id>/', views.DeleteEmployee, name='delete_employee'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('menu1/',views.More_Menu_1),
    path('menu2/',views.More_Menu_2),
    path('menu3/',views.More_Menu_3),
    path('menu4/',views.More_Menu_4),
    path('menu5/',views.More_Menu_5),
    path('menu6/',views.More_Menu_6),
]