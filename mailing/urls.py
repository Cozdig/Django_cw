from django.urls import path
from mailing.apps import MailingConfig
from .views import RecipientCreateView, RecipientListView, RecipientUpdateView, RecipientDetailView, RecipientDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('create_recipient/', RecipientCreateView.as_view(), name="create_recipient"),
    path('', RecipientListView.as_view(), name="recipient_list"),
    path('<int:pk>/', RecipientDetailView.as_view(), name="recipient_detail"),
    path('<int:pk>/edit/', RecipientUpdateView.as_view(), name="recipient_edit"),
    path('<int:pk>/delete/', RecipientDeleteView.as_view(), name="recipient_delete"),

]