from blog.models import Post, Topic
from django import forms


class CreatePost(forms.ModelForm):

    class Meta:
        model = Post 
        fields = [
            "title",
            "topic",
            "post_image",
            "content"
        ]

class UpdatePost(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = [
            "title",
            "topic",
            "post_image",
            "content"
        ]