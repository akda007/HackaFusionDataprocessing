from . import views
from django.urls import path


urlpatterns = [
    path("instructor", views.generate_chart_instructor, name='data-list-create'),
    path("instructor/<int:id>", views.generate_chart_instructor, name='data-list-create'),
    path("student", views.generate_chart_student, name='data-list-create')
]