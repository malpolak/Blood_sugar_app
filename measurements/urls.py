from django.urls import path
from . import views

urlpatterns = [
    path("", views.measurement_list, name="measurement_list"),
    path("measurements", views.measurement_list, name="measurement_list"),
    path("measurement_detail/<int:measurement_id>", views.measurement_detail, name="measurement_detail"),
    path('measurement/<int:measurement_id>/delete/', views.measurement_delete, name="measurement_delete"),

]