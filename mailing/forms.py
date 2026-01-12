from django import forms
from .models import Recipient

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