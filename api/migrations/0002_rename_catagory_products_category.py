# Generated by Django 4.2 on 2023-06-09 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='catagory',
            new_name='category',
        ),
    ]
