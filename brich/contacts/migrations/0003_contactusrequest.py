# Generated by Django 4.2.5 on 2023-09-12 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_callbackrequest_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('nature_of_business', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('postcode', models.CharField(max_length=10)),
                ('contact_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('needs_description', models.TextField()),
            ],
        ),
    ]
