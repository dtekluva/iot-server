# Generated by Django 2.0 on 2018-09-07 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0003_auto_20180907_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='trader',
            name='cell_name',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]
