# Generated by Django 4.0.2 on 2022-02-04 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_reviews'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name_plural': 'Reviews'},
        ),
        migrations.RenameField(
            model_name='reviews',
            old_name='avatar',
            new_name='image',
        ),
    ]