from django.db import models
from django.contrib.auth.models import User
from .utils import image_resize
from PIL import Image as pim


class UserProfile(models.Model):
    ACCOUNT_CHOICES = (
        ("Basic", "Basic"),
        ("Premium", "Premium"),
        ("Enterprise", "Enterprise"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=15,
                            choices=ACCOUNT_CHOICES,
                            default="Basic")

    def __str__(self):
        return str(self.user)



class ImageField(models.ImageField):
    def value_to_string(self, obj):
        return obj.image.url


class Image(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    image_original = models.ImageField(blank=True, null=True)
    image_200 = models.ImageField(blank=True, null=True)
    image_400 = models.ImageField(blank=True, null=True)

    def save(self, *args, **kwargs):
        try:
            with pim.open(self.image_200) as img:
                width, height = img.size
                image_resize(self.image_200, width, 200)
                super().save(*args, **kwargs)
        except:
            pass
        try:
            with pim.open(self.image_400) as img:
                width, height = img.size
                image_resize(self.image_400, width, 400)
                super().save(*args, **kwargs)
        except:
            pass

    def __str__(self):
        return str(self.user.user) + " | filename: " + self.image_original.name

