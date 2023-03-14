from django import forms
from .models import ContactUser, Comment, Reply


class ContactUserForm(forms.ModelForm):
    class Meta:
        model = ContactUser
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = '__all__'
