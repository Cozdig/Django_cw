from django import forms
from .models import Recipient, Message

class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ['email', 'fullname', 'comment']

    def __init__(self, *args, **kwargs):
        super(RecipientForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите email получателя'
        })

        self.fields['fullname'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите ФИО получателя'
        })

        self.fields['comment'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите текст для получателя'
        })

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['topic', 'content']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        self.fields['topic'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите тему письма'
        })

        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите содержимое письма'
        })
