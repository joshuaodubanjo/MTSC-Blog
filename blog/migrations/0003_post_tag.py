# Generated by Django 4.2.1 on 2023-05-17 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_tag_alter_category_options_alter_post_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="tag",
            field=models.ManyToManyField(to="blog.tag"),
        ),
    ]