# Generated by Django 2.0 on 2018-09-07 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0004_trader_cell_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trader',
            name='business_worth',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
