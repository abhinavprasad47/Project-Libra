# Generated by Django 2.1.5 on 2019-02-07 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0022_auto_20190207_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barcode',
            name='number_code',
        ),
    ]