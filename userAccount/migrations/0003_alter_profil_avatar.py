# Generated by Django 3.2 on 2022-03-18 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0002_auto_20220318_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='avatar',
            field=models.ImageField(blank=True, default='usericon.png', null=True, upload_to='avatars/'),
        ),
    ]
