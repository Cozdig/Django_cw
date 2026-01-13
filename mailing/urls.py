from django.urls import path
from mailing.apps import MailingConfig
from .views import RecipientCreateView, RecipientListView, RecipientUpdateView, RecipientDetailView, RecipientDeleteView
from .views import MessageListView, MessageCreateView, MessageDeleteView, MessageDetailView, MessageUpdateView

app_name = MailingConfig.name

urlpatterns = [
    path('create_recipient/', RecipientCreateView.as_view(), name="create_recipient"),
    path('', RecipientListView.as_view(), name="recipient_list"),
    path('<int:pk>/', RecipientDetailView.as_view(), name="recipient_detail"),
    path('<int:pk>/edit/', RecipientUpdateView.as_view(), name="recipient_edit"),
    path('<int:pk>/delete/', RecipientDeleteView.as_view(), name="recipient_delete"),
    path('messages/create_message/', MessageCreateView.as_view(), name="create_message"),
    path('messages/', MessageListView.as_view(), name="message_list"),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name="message_detail"),
    path('messages/<int:pk>/edit/', MessageUpdateView.as_view(), name="message_edit"),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name="message_delete")

]