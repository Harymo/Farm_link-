# Generated by Django 5.0.3 on 2024-03-29 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproduct', '0006_sell_category_sell_cost_price_sell_harvest_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sell',
            name='name',
        ),
    ]