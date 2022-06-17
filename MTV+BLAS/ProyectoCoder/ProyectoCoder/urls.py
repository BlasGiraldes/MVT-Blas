from django.contrib import admin
from django.urls import path
from AppCoder.views import familia, template1


urlpatterns = [
    path('admin/', admin.site.urls),
    path('familia/', familia),
    path('template/', template1),
]
