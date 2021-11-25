from django.db import migrations
from django.conf import settings


def update_site_name(apps, schema_editor):
    SiteModel = apps.get_model('sites', 'Site')
    domain = '0.0.0.0:8000/'

    SiteModel.objects.update_or_create(
        pk=settings.SITE_ID,
        defaults={'domain': domain,
                  'name': domain}
    )


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.RunPython(update_site_name),
    ]
