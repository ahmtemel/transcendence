# Generated by Django 4.0 on 2024-10-29 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user', '0003_chatrooms_chatuserlist_chatmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfriendslist',
            name='blocked_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user'),
        ),
        migrations.AddField(
            model_name='userfriendslist',
            name='friend_block',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='chatrooms',
            name='roomName',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='photo',
            field=models.ImageField(blank=True, default='profil_photo/default.png', null=True, upload_to='profil_photo/'),
        ),
    ]
