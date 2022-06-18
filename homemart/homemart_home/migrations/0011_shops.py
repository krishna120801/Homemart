# Generated by Django 3.2.3 on 2021-06-06 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homemart_home', '0010_cart_shopname'),
    ]

    operations = [
        migrations.CreateModel(
            name='shops',
            fields=[
                ('cartid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('price', models.CharField(max_length=10, null=True)),
                ('shopid', models.CharField(max_length=10)),
                ('shopname', models.CharField(max_length=100)),
            ],
        ),
    ]