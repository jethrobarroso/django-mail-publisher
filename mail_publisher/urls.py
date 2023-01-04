from django.urls import path
from mail_publisher import views

app_name = "mail"

urlpatterns = [
    # no auth
    path(
        "mails/",
        views.MailPublisher.as_view()
    ) 
]
