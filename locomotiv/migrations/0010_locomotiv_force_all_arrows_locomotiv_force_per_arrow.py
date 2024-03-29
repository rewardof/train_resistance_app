# Generated by Django 4.0.1 on 2022-03-24 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locomotiv', '0009_trainresistancedata_all_idle_resistance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='locomotiv',
            name='force_all_arrows',
            field=models.FloatField(default=6000, verbose_name='Barcha o‘qga bosilishidagi haqiqiy kuchi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='locomotiv',
            name='force_per_arrow',
            field=models.FloatField(default=72000, verbose_name='Bitta o‘qga bosilishidagi haqiqiy kuchi'),
            preserve_default=False,
        ),
    ]
