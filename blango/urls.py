from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path("", blog.views.index),
    path('admin/', admin.site.urls),
]
