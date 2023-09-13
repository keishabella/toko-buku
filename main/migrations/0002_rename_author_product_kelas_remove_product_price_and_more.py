# Generated by Django 4.2.5 on 2023-09-12 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='author',
            new_name='kelas',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='nama',
            field=models.CharField(default='', max_length=255),
        ),
    ]
