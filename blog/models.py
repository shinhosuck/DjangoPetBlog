from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from PIL import Image


class Topic(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_image = models.ImageField(default="default_post_img.jpg", upload_to="post_images")
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, blank=True, related_name="post_likes")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.post_image.path)
        if img.width > 600 and img.height > 600:
            new_img = (500, 500)
            img.thumbnail(new_img)
            img.save(self.post_image.path)

    class Meta:
        ordering = ["-date_posted"]

