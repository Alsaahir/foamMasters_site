from django import forms
from .models import Subscriber, SentMail, RecievedMail
from django.contrib.auth import authenticate

class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email', ]
    
class MessageForm(forms.ModelForm):
    class Meta:
        model = SentMail
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

class ContactForm(forms.ModelForm):
    class Meta:
        model = RecievedMail
        fields = '__all__'