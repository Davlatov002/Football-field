# Generated by Django 5.0.3 on 2024-03-16 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footballfield', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodballfield',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
