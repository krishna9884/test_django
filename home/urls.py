from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('info/',views.infofg, name='info'),
    path('info/delete/<int:id>', views.delete, name='delete'),
    path('info/update/<int:id>', views.update, name='update'),
    path('info/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('search/',views.search, name='search'),
]