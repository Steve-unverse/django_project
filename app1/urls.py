from django.urls import path
from .views import first_view,last_view
urlpatterns= [
    path('',first_view,name = 'first_view'),
    path('last_view',last_view,name = 'last_view')
]