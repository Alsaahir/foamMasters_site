from django import forms
from .models import Subscriber, MailMassage
from django.contrib.auth import authenticate

class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email', ]
    
class MessageForm(forms.ModelForm):
    class Meta:
        model = MailMassage
        fields = '__all__'

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("The user does not exist")
            if not user.check_password(password):
                raise forms.validationError("The password was incorrect")
                if not user.is_active:
                    raise forms.validationError("The user is no longer active")
            return super(UserLoginForm, self).clean(*args, **kwargs)

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)