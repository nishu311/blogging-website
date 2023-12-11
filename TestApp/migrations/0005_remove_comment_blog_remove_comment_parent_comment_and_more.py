# Generated by Django 4.2 on 2023-05-31 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("TestApp", "0004_blogpost_comment_profile_delete_post"),
    ]

    operations = [
        migrations.RemoveField(model_name="comment", name="blog",),
        migrations.RemoveField(model_name="comment", name="parent_comment",),
        migrations.RemoveField(model_name="comment", name="user",),
        migrations.RemoveField(model_name="profile", name="user",),
        migrations.DeleteModel(name="BlogPost",),
        migrations.DeleteModel(name="Comment",),
        migrations.DeleteModel(name="Profile",),
    ]