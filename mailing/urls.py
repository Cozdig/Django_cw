from django.urls import path
from mailing.apps import MailingConfig
from .views import RecipientCreateView, RecipientListView, RecipientUpdateView, RecipientDetailView, RecipientDeleteView
from .views import MessageListView, MessageCreateView, MessageDeleteView, MessageDetailView, MessageUpdateView
from .views import MailingsDeleteView, MailingsCreateView, MailingsDetailView, MailingsUpdateView, MailingsListView

app_name = MailingConfig.name

urlpatterns = [
    path('recipients/create_recipient/', RecipientCreateView.as_view(), name="create_recipient"),
    path('recipients/', RecipientListView.as_view(), name="recipient_list"),
    path('recipients/<int:pk>/', RecipientDetailView.as_view(), name="recipient_detail"),
    path('recipients/<int:pk>/edit/', RecipientUpdateView.as_view(), name="recipient_edit"),
    path('recipients/<int:pk>/delete/', RecipientDeleteView.as_view(), name="recipient_delete"),
    path('messages/create_message/', MessageCreateView.as_view(), name="create_message"),
    path('messages/', MessageListView.as_view(), name="message_list"),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name="message_detail"),
    path('messages/<int:pk>/edit/', MessageUpdateView.as_view(), name="message_edit"),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name="message_delete"),
    path('create_mailing/', MailingsCreateView.as_view(), name="create_mailing"),
    path('', MailingsListView.as_view(), name="mailings_list"),
    path('<int:pk>/', MailingsDetailView.as_view(), name="mailing_detail"),
    path('<int:pk>/edit/', MailingsUpdateView.as_view(), name="mailing_edit"),
    path('<int:pk>/delete/', MailingsDeleteView.as_view(), name="mailing_delete")
]