# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-25 01:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mainshow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackid', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=50)),
                ('img', models.CharField(max_length=200)),
                ('categoryid', models.CharField(max_length=16)),
                ('brandname', models.CharField(max_length=50)),
                ('img1', models.CharField(max_length=200)),
                ('childid1', models.CharField(max_length=16)),
                ('productid1', models.CharField(max_length=16)),
                ('longname1', models.CharField(max_length=100)),
                ('price1', models.FloatField(default=0)),
                ('marketprice1', models.FloatField(default=0)),
                ('img2', models.CharField(max_length=200)),
                ('childid2', models.CharField(max_length=16)),
                ('productid2', models.CharField(max_length=16)),
                ('longname2', models.CharField(max_length=100)),
                ('price2', models.FloatField(default=0)),
                ('marketprice2', models.FloatField(default=0)),
                ('img3', models.CharField(max_length=200)),
                ('childid3', models.CharField(max_length=16)),
                ('productid3', models.CharField(max_length=16)),
                ('longname3', models.CharField(max_length=100)),
                ('price3', models.FloatField(default=0)),
                ('marketprice3', models.FloatField(default=0)),
            ],
        ),
    ]
