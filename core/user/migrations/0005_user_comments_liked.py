# Generated by Django 4.0 on 2023-10-12 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_comment', '0001_initial'),
        ('core_user', '0004_user_posts_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='comments_liked',
            field=models.ManyToManyField(related_name='commented_by', to='core_comment.Comment'),
        ),
    ]
