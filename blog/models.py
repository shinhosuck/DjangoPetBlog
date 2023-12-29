from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from PIL import Image
import uuid

class Topic(models.Model):
    name = models.CharField(max_length=50)
    topic_image = models.ImageField(upload_to="topic_images")
    image_url = models.URLField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    total_post = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_image = models.ImageField(default="post_images/default.webp", upload_to="post_images")
    image_url = models.URLField(null=True, blank=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, blank=True, related_name="post_likes")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.post_image:
            self.post_image = '/post_images/default.jpg'
        super().save(*args, **kwargs)
        img = Image.open(self.post_image.path)
        if img.width > 600 and img.height > 600:
            new_img = (500, 500)
            img.thumbnail(new_img)
            img.save(self.post_image.path)

    class Meta:
        ordering = ["-date_posted"]

