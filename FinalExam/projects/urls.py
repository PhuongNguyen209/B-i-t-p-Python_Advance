from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    # path("", views.profile, name="profile"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]