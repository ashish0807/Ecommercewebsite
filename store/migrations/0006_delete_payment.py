# Generated by Django 5.0.3 on 2024-04-27 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
