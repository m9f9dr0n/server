from django.urls import path

from women.views import *

urlpatterns = [

    path('', index),
    path('liceum/', index),
    path('cats/<int:cat_id>/', categories)

]



