# Generated by Django 2.1.4 on 2020-01-11 17:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Purchased at')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_uuid', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('sold_quantity', models.IntegerField(default=0)),
                ('purchase_price_per_unit', models.FloatField()),
                ('sale_price_per_unit', models.FloatField()),
                ('purchase_id', models.ForeignKey(on_delete=None, to='transaction.Purchase')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Sold at')),
                ('discount', models.FloatField(default=0.0)),
            ],
            options={
                'permissions': (('read_item', 'Can read item'),),
            },
        ),
        migrations.CreateModel(
            name='SaleProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_uuid', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('sale_id', models.ForeignKey(on_delete=None, to='transaction.Sale')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='purchase',
            name='supplier_id',
            field=models.ForeignKey(on_delete=None, to='transaction.Supplier'),
        ),
    ]
