from django.urls import path
from . import views

urlpatterns = [
    path("",views.employee_form,name="employee-insert"),
    path("<int:id>/edit/",views.employee_form,name="employee_update"),
    path("<int:id>/delete/",views.employee_delete,name="employee_delete"),
    path("list/",views.employee_list ,name="employee_list")
]
