# Generated by Django 4.1.4 on 2022-12-29 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0002_alter_advertisement_options_alter_advertisement_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='creator',
            new_name='user',
        ),
    ]
