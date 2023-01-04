from django.contrib import admin
from django.urls import path, include
from mail_publisher.urls import urlpatterns as mail_publisher_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(mail_publisher_urls), name='mail')
]
