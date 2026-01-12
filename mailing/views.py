from django.shortcuts import render
from django.views.generic import DetailView, DeleteView, ListView
from django.views.generic.edit import CreateView, UpdateView

from mailing.forms import RecipientForm

from mailing.models import Recipient

# Create your views here.

class RecipientCreateView(CreateView):
    model = Recipient
    form_class = RecipientForm
    template_name = 'mailing/recipient_form.html'
    success_url = '/mailing/'

class RecipientListView(ListView):
    model = Recipient
    template_name = "mailing/recipient_list.html"
    context_object_name = "recipients"

