# Generated by Django 4.2.11 on 2024-04-08 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total',
            new_name='total_sum',
        ),
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card')], max_length=4),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('D', 'Delivered'), ('ND', 'Not Delivered')], max_length=2),
        ),
    ]
