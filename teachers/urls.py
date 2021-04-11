from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/5/
    path('', views.teacher_profile_page, name='teacher_profile_page'),
]