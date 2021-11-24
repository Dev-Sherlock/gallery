from django.db import models
from django.contrib.auth.models import User
from .utils import image_resize
from PIL import Image as pim
from django.db import migrations
from django.conf import settings


def update_site_name(apps, schema_editor):
    SiteModel = apps.get_model('sites', 'Site')
    domain = 'http://0.0.0.0:8000/'

    SiteModel.objects.update_or_create(
        pk=settings.SITE_ID,
        defaults={'domain': domain,
                  'name': domain}
    )


class Migration(migrations.Migration):

    dependencies = [
        # Make sure the dependency that was here by default is also included here
        ('sites', '0001_initial'), # Required to reference `sites` in `apps.get_model()`
    ]

    operations = [
        migrations.RunPython(update_site_name),
    ]


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
        with pim.open(self.image_200) as img:
            width, height = img.size
            image_resize(self.image_200, width, 200)
            super().save(*args, **kwargs)
        with pim.open(self.image_400) as img:
            width, height = img.size
            image_resize(self.image_400, width, 400)
            super().save(*args, **kwargs)

    def __str__(self):
        return str(self.user.user) + " | filename: " + self.image_original.name

