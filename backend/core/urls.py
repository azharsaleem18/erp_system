from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.conf.urls.i18n import i18n_patterns

admin.sites.AdminSite.site_header = 'Business Management System'
admin.sites.AdminSite.site_title = 'Business Management System'
admin.sites.AdminSite.index_title = 'BMS Adminpanel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('custom_auth.urls')),
]
