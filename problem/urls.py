from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^(?P<problem_id>[0-9]+)/', views.problem, name='problem'),
]
