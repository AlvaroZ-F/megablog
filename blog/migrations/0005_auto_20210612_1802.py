# Generated by Django 3.0.8 on 2021-06-12 18:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]