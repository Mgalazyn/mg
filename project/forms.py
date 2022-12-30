from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Message

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2' ]


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['email', 'subject', 'body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({'class':'input-field', 'placeholder': 'Add your email: '})

        self.fields['subject'].widget.attrs.update({'class':'input-field', 'placeholder': 'Subject: '})

        self.fields['body'].widget.attrs.update({'class':'input-field textarea-field', 'placeholder': 'Your message: '})