from django.urls import path
from mailing.apps import MailingConfig
from .views import RecipientCreateView, RecipientListView

app_name = MailingConfig.name

urlpatterns = [
    path('create_recipient/', RecipientCreateView.as_view(), name="create_recipient"),
    path('', RecipientListView.as_view(), name="recipient_list"),

]