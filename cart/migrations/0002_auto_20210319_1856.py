# Generated by Django 2.1 on 2021-03-19 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='image_url',
            field=models.CharField(default=None, max_length=4088),
        ),
        migrations.AddField(
            model_name='cart',
            name='productname',
            field=models.CharField(default=None, max_length=80),
        ),
        migrations.AlterField(
            model_name='cart',
            name='productkey',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
