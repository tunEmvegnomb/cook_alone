# Generated by Django 4.0.5 on 2022-06-09 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_alter_recipe_timecost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='author',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='img_file',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='updated_at',
        ),
    ]
