# Generated by Django 4.2.4 on 2023-08-15 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_food_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(choices=[('default', 'Select Food Type'), ('Pizza', 'Pizza'), ('Burger', 'Burger'), ('Rice', 'Rice'), ('Coffee', 'Coffee'), ('Chicken & Chips', 'Chicken & Chips'), ('Ice-Cream', 'Ice-Cream')], default='', max_length=100),
        ),
    ]