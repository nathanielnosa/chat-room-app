# Generated by Django 3.2.7 on 2021-12-13 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_alter_message_msg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='msg',
            field=models.CharField(max_length=500),
        ),
    ]
