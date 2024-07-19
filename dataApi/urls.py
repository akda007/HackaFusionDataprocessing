from . import views
from django.urls import path


urlpatterns = [
    path("data/instructor", views.generate_chart_instructor, name='data-list-create'),
    path("data/student", views.generate_chart_student, name='data-list-create')
]