from django.db import models
from PIL import Image
from django.contrib.auth.models import User 


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="user_images")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.width > 400 or img.height > 400:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.image.path)
