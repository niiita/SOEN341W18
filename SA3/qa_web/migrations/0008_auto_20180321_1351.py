# Generated by Django 2.0 on 2018-03-21 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa_web', '0007_user_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_img'),
        ),
    ]
