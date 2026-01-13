from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, ListView
from django.views.generic.edit import CreateView, UpdateView

from mailing.forms import RecipientForm, MessageForm

from mailing.models import Recipient, Message

# Create your views here.

# Recipient
class RecipientCreateView(CreateView):
    model = Recipient
    form_class = RecipientForm
    title = "Добавление получателя"
    template_name = 'mailing/recipient_form.html'
    success_url = reverse_lazy("mailing:recipient_list")

class RecipientListView(ListView):
    model = Recipient
    template_name = "mailing/recipient_list.html"
    context_object_name = "recipients"

class RecipientDetailView(DetailView):
    model = Recipient
    template_name = 'mailing/recipient_detail.html'
    context_object_name = "recipient"

class RecipientUpdateView(UpdateView):
    model = Recipient
    form_class = RecipientForm
    title = "Редактирование получателя"
    template_name = 'mailing/recipient_form.html'
    success_url = reverse_lazy("mailing:recipient_list")

class RecipientDeleteView(DeleteView):
    model = Recipient
    template_name = 'mailing/recipient_confirm_delete.html'
    success_url = reverse_lazy("mailing:recipient_list")

# Message
class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    title = "Добавление письма"
    template_name = 'mailing/message_form.html'
    success_url = reverse_lazy("mailing:message_list")

class MessageListView(ListView):
    model = Message
    template_name = "mailing/message_list.html"
    context_object_name = "messages"

class MessageDetailView(DetailView):
    model = Message
    template_name = 'mailing/message_detail.html'
    context_object_name = "message"

class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    title = "Редактирование письма"
    template_name = 'mailing/message_form.html'
    success_url = reverse_lazy("mailing:message_list")

class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'mailing/message_confirm_delete.html'
    success_url = reverse_lazy("mailing:message_list")