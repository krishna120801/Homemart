# Generated by Django 3.2.3 on 2021-06-06 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homemart_home', '0015_auto_20210607_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='shopid',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='shopName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shops',
            name='shopid',
            field=models.CharField(max_length=25),
        ),
    ]
