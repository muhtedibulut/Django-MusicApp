from django.urls import path
from . import views

urlpatterns = [

    path('', views.musicianList, name='musicianList'),
    path('view/<int:pk>', views.musicianView, name='musicianView'),
    path('new', views.musicianCreate, name='musicianNew'),
    path('edit/<int:pk>', views.musicianUpdate, name='musicianEdit'),
    path('delete/<int:pk>', views.musicianDelete, name='musicianDelete'),
]