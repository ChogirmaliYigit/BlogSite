from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=250, required=True)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'bio', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.bio = self.cleaned_data.get('bio')

        if commit:
            user.save()
        return user


