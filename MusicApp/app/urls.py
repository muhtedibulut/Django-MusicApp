from django.urls import path
from . import views

urlpatterns = [

    path('', views.musician_list, name='musicianList'),
    path('view/<int:pk>', views.musician_view, name='musicianView'),
    path('new', views.musician_create, name='musicianNew'),
    path('edit/<int:pk>', views.musician_update, name='musicianEdit'),
    path('delete/<int:pk>', views.musician_delete, name='musicianDelete'),
]