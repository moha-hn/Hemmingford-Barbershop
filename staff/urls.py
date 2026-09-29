from django.urls import path
from . import views

app_name = "staff"

urlpatterns = [
    path("<int:pk>/", views.staff_detail, name="detail"),
]
