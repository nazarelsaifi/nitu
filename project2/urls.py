"""project2 URL Configuration

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
from django.urls import include, path
from overview.views import customer_message, deleteService, deleteBooking, overview, website, contact, location, delete_customer_message
from booking.views import save_customer_data, select_date, select_service, add_service, delete_service, customer_info, safe_date,thank_you
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("django.contrib.auth.urls")),
    path('overview/', overview),

    path('', website, name="home"),
    path('contact/', contact, name="contact"),
    path('location/', location, name="location"),

    path('overview/deleteS/<int:id>/', deleteService),
    path('overview/deleteB/<int:id>/', deleteBooking),
    path('overview/delete_customer_message/<int:id>/', delete_customer_message, name='delete_customer_message'),

    path('select_service/', select_service, name='select_service'),
    path('select_service/<int:id>/', add_service, name='add_service'),
    path('select_service/delete_service/<int:id>/', delete_service, name='delete_service'),
    path('select_date/', select_date, name='select_date'),
    path('select_date/<str:datestring>/', safe_date, name='safe_date'),
    path('customer_info/', customer_info, name='customer_info'),
    path('customer_info/<str:datestring>/', customer_info, name='customer_info'),
    path('thank_you/', thank_you, name='thank_you'),
    path('save_customer_data/', save_customer_data, name='save_customer_data'),
    path('we_will_contact_you.html/', customer_message, name='customer_message'),
]
