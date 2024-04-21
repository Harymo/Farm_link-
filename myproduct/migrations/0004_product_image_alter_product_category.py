# Generated by Django 5.0.3 on 2024-03-29 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproduct', '0003_alter_make_order_options_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='profile_images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Fruit', 'Fruit'), ('Grains', 'Grains'), ('Vegetables', 'Vegetables'), ('Legumes', 'Legumes'), ('Oilseeds', 'Oilseeds'), ('Roots and Tubers', 'Roots and Tubers'), ('Nuts', 'Nuts'), ('Animal', 'Animal'), ('Poetry', 'Poetry'), ('Tropical Crops', 'Tropical Crops'), ('Indistrial crops', 'Indusctrial Crop')], max_length=100, null=True),
        ),
    ]
