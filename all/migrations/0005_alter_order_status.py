# Generated by Django 4.1.5 on 2023-05-23 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all', '0004_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Pending', 'Pending'), ('out of order', 'out of order'), ('in progress', 'in progress')], max_length=200, null=True),
        ),
    ]
