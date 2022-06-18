# Generated by Django 3.2.5 on 2022-06-18 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homemart_home', '0016_auto_20210607_0111'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=25)),
                ('l_name', models.CharField(max_length=25)),
                ('phone_no', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=25)),
                ('Address1', models.CharField(max_length=75)),
                ('Address2', models.CharField(max_length=75)),
                ('Post_Zip', models.IntegerField(max_length=10)),
                ('Town_City', models.CharField(max_length=25)),
                ('Additional', models.TextField(max_length=100)),
            ],
        ),
    ]