from django.urls import path
from . import views
urlpatterns = [
    path('',views.testing,name = 'testing'),
    path('/delete/<int:id>',views.delete,name = 'delete'),
]