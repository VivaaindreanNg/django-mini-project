# Generated by Django 3.2.3 on 2021-05-22 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0003_auto_20210522_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claimsmodel',
            name='mobileNo',
            field=models.IntegerField(null=True, verbose_name='Mobile No.'),
        ),
    ]