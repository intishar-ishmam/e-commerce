# Generated by Django 2.2.1 on 2021-10-20 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'clients',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_no', models.CharField(default=None, max_length=10)),
                ('cart_no', models.CharField(max_length=10)),
                ('full_name', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=255)),
                ('cost', models.IntegerField()),
                ('delivery_fees', models.IntegerField()),
                ('total_cost', models.IntegerField()),
                ('status', models.CharField(blank=True, choices=[('accepted', 'Accepted'), ('delivered', 'Delivered'), ('canceled', 'Canceled'), ('declined', 'Declined'), ('returned', 'Returned')], max_length=100, null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Clients')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
