# Generated by Django 4.2.5 on 2023-10-17 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_creatorscallbackrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactusrequest',
            name='contact_name',
        ),
        migrations.RemoveField(
            model_name='contactusrequest',
            name='needs_description',
        ),
    ]