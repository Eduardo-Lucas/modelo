from django.urls import path

from apps.core.views import *

urlpatterns = [
    path('', index, name='index'),

]
