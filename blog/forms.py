from django import forms
from .models import ContactUser, Comment, Reply, Feedback


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

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('full_name_feedback', 'image_feedback', 'email_feedback', 'field_feedback', 'feedback')
