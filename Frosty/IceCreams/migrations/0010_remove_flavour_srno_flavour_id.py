# Generated by Django 4.0 on 2022-01-02 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IceCreams', '0009_alter_flavour_srno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flavour',
            name='srno',
        ),
        migrations.AddField(
            model_name='flavour',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
