# Generated by Django 2.1 on 2021-03-15 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AddField(
            model_name='product',
            name='pid',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
    ]
