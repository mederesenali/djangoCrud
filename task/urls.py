from django.conf.urls import url
from django.contrib import admin

from task import views

urlpatterns = [
    url(r'^$', views.getHomePage,name='getHomePage'),
    url('doneTask/', views.getDoneTasks,name='getDoneTasks'),

]