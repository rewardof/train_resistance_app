# Generated by Django 4.0.1 on 2022-03-01 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locomotiv', '0003_totaldatavagon_load_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='locomotiv',
            name='lenght',
            field=models.FloatField(default=20, verbose_name='Lokomotiv uzunligi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='locomotiv',
            name='number_arrows',
            field=models.SmallIntegerField(default=12, verbose_name="O'qlar soni"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='locomotiv',
            name='weigth',
            field=models.FloatField(default=120, verbose_name="Lokomotiv og'irligi"),
            preserve_default=False,
        ),
    ]
