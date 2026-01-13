from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, ListView
from django.views.generic.edit import CreateView, UpdateView

from mailing.forms import RecipientForm, MessageForm, MailingForm

from mailing.models import Recipient, Message, Mailings


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
    template_name = "mailing/recipients_list.html"
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
    template_name = "mailing/messages_list.html"
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

# Mailing
class MailingsCreateView(CreateView):
    model = Mailings
    form_class = MailingForm
    title = "Создание рассылки"
    template_name = 'mailing/mailing_form.html'
    success_url = reverse_lazy("mailing:mailings_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.update_status()
        return response

class MailingsListView(ListView):
    model = Mailings
    template_name = 'mailing/mailings_list.html'
    context_object_name = 'mailings'

    def get_queryset(self):
        queryset = super().get_queryset()

        for mailing in queryset:
            mailing.update_status()

        return queryset

class MailingsDetailView(DetailView):
    model = Mailings
    template_name = 'mailing/mailing_detail.html'
    context_object_name = 'mailing'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.update_status()
        return obj

class MailingsUpdateView(UpdateView):
    model = Mailings
    form_class = MailingForm
    title = "Редактирование рассылки"
    template_name = 'mailing/mailing_form.html'
    success_url = reverse_lazy("mailing:mailings_list")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.update_status()
        return obj

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.update_status()
        return response

class MailingsDeleteView(DeleteView):
    model = Mailings
    template_name = 'mailing/mailing_confirm_delete.html'
    success_url = reverse_lazy("mailing:mailings_list")