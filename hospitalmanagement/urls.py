"""hospitalmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospital.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', a_login, name="a_login"),
    path('a_home', a_home, name="a_home"),
    path('about', about, name='about'),
    path('a_logout', a_logout, name="a_logout"),
    path('contact', contact, name="contact"),
    path('view_doctor', view_doctor, name="view_doctor"),
    path('add_doctor', add_doctor, name="add_doctor"),
    path('delete_doctor/<int:pid>', delete_doctor, name="delete_doctor"),
    path('view_patient', view_patient, name="view_patient"),
    path('add_patient', add_patient, name="add_patient"),
    path('delete_patient/<int:pid>', delete_patient, name="delete_patient"),
    path('view_appointment', view_appointment, name="view_appointment"),
    path('add_appointment', add_appointment, name="add_appointment"),
    path('delete_appointment/<int:pid>', delete_appointment, name="delete_appointment"),
    path('edit_doctor/<int:pid>', edit_doctor, name="edit_doctor"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
