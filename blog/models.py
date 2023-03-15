from datetime import datetime
from django.db import models

class Admin(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=250)
    username = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=200)
    bio = models.TextField()
    level = models.CharField(max_length=300)
    fields = models.TextField()
    image = models.ImageField(upload_to='admins/', default='admins/default-admin.jpg')
    address = models.TextField(default='', null=True, blank=True)

    def __str__(self) -> str:
        return f'Admin - {self.full_name}'

class SocialLink(models.Model):
    title = models.CharField(max_length=300)
    link = models.URLField()
    icon = models.CharField(max_length=300, help_text="class atributi uchun qo'yiladigan class nomi")
    user = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='socials')

    def __str__(self) -> str:
        return f'Social - {self.title}'

class Skill(models.Model):
    user = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='skills')
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    protsent = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return f'Skill - {self.title}'

class Service(models.Model):
    user = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    icon = models.CharField(max_length=300, help_text="class atributi uchun qo'yiladigan class nomi")

    def __str__(self) -> str:
        return f'Service - {self.title}'

class Portfolio(models.Model):
    user = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='portfolios')
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')
    category = models.CharField(max_length=100)
    client = models.CharField(max_length=500)
    url = models.URLField(null=True, blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Portfolio - {self.title}'

    class Meta:
        verbose_name_plural = 'Portfolioes'

class Feedback(models.Model):
    full_name_feedback = models.CharField(max_length=150, blank=True, null=True, default='Anonymous User')
    email_feedback = models.EmailField(max_length=250, blank=True, null=True)
    field_feedback = models.CharField(max_length=200, default='None')
    feedback = models.TextField()
    image_feedback = models.ImageField(upload_to='feedbacks/', null=True, blank=True, default='feedbacks/anonymous-user.jpg')
    show = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'Feedback - {self.full_name_feedback}'

class Tag(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Tag - {self.title}'

class Post(models.Model):
    title = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/')
    author = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Post - {self.title}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', default=1)
    full_name = models.CharField(max_length=200, null=True, blank=True, default='Anonymous user')
    content = models.TextField()
    image = models.ImageField(upload_to='comments/', null=True, blank=True, default='comments/anonymous-user.jpg')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Comment - {self.pk}'

class Reply(models.Model):
    full_name_reply = models.CharField(max_length=200, null=True, blank=True, default='Anonymous user')
    content_reply = models.TextField()
    image_reply = models.ImageField(upload_to='replies/', null=True, blank=True, default='replies/anonymous-user.jpg')
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Reply - {self.pk}'

    class Meta:
        verbose_name_plural = 'Replies'

class ContactUser(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self) -> str:
        return f'Contact user - {self.email}'