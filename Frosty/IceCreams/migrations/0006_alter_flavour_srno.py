# Generated by Django 4.0 on 2022-01-02 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IceCreams', '0005_alter_flavour_srno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flavour',
            name='srno',
            field=models.CharField(default='', max_length=100, primary_key=True, serialize=False),
        ),
    ]
