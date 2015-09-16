# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('changuito', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=b'', max_length=255)),
                ('last_name', models.CharField(default=b'', max_length=255)),
                ('email', models.CharField(default=b'', max_length=255, blank=True)),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(max_length=255, blank=True)),
                ('suburb', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('postcode', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'BillingAddress',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(default=1, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to=b'static/', blank=True)),
                ('url', models.URLField(max_length=1024, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('submit_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default=b'inactive', max_length=255)),
                ('payment_proccessed', models.BooleanField(default=False)),
                ('total_amount', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField(null=True)),
                ('cart_id', models.ForeignKey(to='changuito.Cart')),
                ('customer_id', models.ForeignKey(to='cart.Customer')),
            ],
            options={
                'verbose_name': 'Order',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255, blank=True)),
                ('image', models.CharField(max_length=1024, blank=True)),
                ('url', models.URLField(max_length=1024, blank=True)),
                ('unit_price', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True, blank=True)),
                ('weight', models.PositiveIntegerField(default=1)),
                ('length', models.PositiveIntegerField(default=10)),
                ('width', models.PositiveIntegerField(default=10)),
                ('height', models.PositiveIntegerField(default=10)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=b'', max_length=255)),
                ('last_name', models.CharField(default=b'', max_length=255)),
                ('email', models.CharField(default=b'', max_length=255, blank=True)),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(max_length=255, blank=True)),
                ('suburb', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('postcode', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('business_name', models.CharField(max_length=255, blank=True)),
                ('customer', models.ForeignKey(to='cart.Customer')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'ShippingAddress',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(max_length=255, blank=True)),
                ('suburb', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('postcode', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('abn', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='customer',
            field=models.ForeignKey(to='cart.Customer'),
        ),
    ]
