# Generated by Django 3.0.2 on 2020-01-18 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200118_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('NONE', 'NONE'), ('M', 'male'), ('F', 'female')], default='NONE', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('NONE', 'NONE'), ('S', 'small'), ('XS', 'extra small'), ('M', 'medium'), ('L', 'large'), ('XL', 'extra large')], default='NONE', max_length=50),
        ),
    ]
