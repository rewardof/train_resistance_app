# Generated by Django 4.0.1 on 2022-02-09 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locomotiv', '0002_trainresistancedata_delete_excel'),
    ]

    operations = [
        migrations.AddField(
            model_name='totaldatavagon',
            name='load_weight',
            field=models.FloatField(default=20, verbose_name="Yuk og'irligi"),
            preserve_default=False,
        ),
    ]