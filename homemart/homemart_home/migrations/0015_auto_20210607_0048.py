# Generated by Django 3.2.3 on 2021-06-06 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homemart_home', '0014_shops'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Big_bazaar_price',
        ),
        migrations.DeleteModel(
            name='D_mart_price',
        ),
        migrations.DeleteModel(
            name='k_mart_price',
        ),
    ]