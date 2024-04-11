from django.contrib import admin
from django.urls import path

from main.views import index, get_menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('<menu_name>', get_menu, name='get_menu'),
]
