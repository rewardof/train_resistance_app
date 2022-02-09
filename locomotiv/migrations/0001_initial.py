# Generated by Django 4.0.1 on 2022-02-08 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Excel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/', verbose_name='Excel file')),
            ],
            options={
                'verbose_name': 'Excel file',
                'verbose_name_plural': 'Excel filelar',
            },
        ),
        migrations.CreateModel(
            name='Locomotiv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locomotiv_name', models.CharField(max_length=32, verbose_name='Lokomotiv nomi')),
                ('locomotiv_seria', models.CharField(max_length=32, verbose_name='Lokomotiv seriyasi')),
                ('locomotiv_number', models.CharField(max_length=32, verbose_name='Lokomotiv raqami')),
                ('type_locomotiv', models.IntegerField(choices=[(1, 'Manyovr Lokomotivi'), (2, 'Poyezd Lokomotivi')], verbose_name='Lokomotiv turi')),
                ('value_ao', models.FloatField(verbose_name='ao qiymati')),
                ('value_bo', models.FloatField(verbose_name='bo qiymati')),
                ('value_co', models.FloatField(verbose_name='co qiymati')),
                ('value_aox', models.FloatField(verbose_name='aox qiymati')),
                ('value_box', models.FloatField(verbose_name='box qiymati')),
                ('value_cox', models.FloatField(verbose_name='cox qiymati')),
                ('is_active', models.BooleanField(default=True, verbose_name='Faol')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Tahrirlangan vaqt')),
            ],
            options={
                'verbose_name': 'Lokomotiv Turi',
                'verbose_name_plural': 'Lokomotiv Turlari',
            },
        ),
        migrations.CreateModel(
            name='TotalDataVagon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_vagon', models.IntegerField(verbose_name='Vagon raqami')),
                ('number_of_arrow', models.SmallIntegerField(verbose_name="O'qlar soni")),
                ('netto_vagon', models.FloatField(verbose_name="Vagon og'irligi")),
                ('length_vagon', models.FloatField(verbose_name='Vagon uzunligi')),
                ('total_weight', models.FloatField(verbose_name="Umumiy og'irlik")),
                ('bullet_weight', models.FloatField(verbose_name="O'qqa tushadigan og'irlik")),
            ],
            options={
                'verbose_name': 'Vagon xarakteristikasi',
                'verbose_name_plural': 'Vagonlar xarakteristikasi',
            },
        ),
        migrations.CreateModel(
            name='VagonResistanceConstant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_ao', models.FloatField(verbose_name='ao qiymati')),
                ('value_bo', models.FloatField(verbose_name='bo qiymati')),
                ('value_co', models.FloatField(verbose_name='co qiymati')),
                ('value_aox', models.FloatField(verbose_name='aox qiymati')),
                ('value_box', models.FloatField(verbose_name='cox qiymati')),
                ('value_cox', models.FloatField(verbose_name='cox qiymati')),
                ('value_ax', models.FloatField(verbose_name='ax qiymati')),
                ('value_bx', models.FloatField(verbose_name='bx qiymati')),
                ('value_cx', models.FloatField(verbose_name='cx qiymati')),
            ],
            options={
                'verbose_name': "Vagon Qarshili uchun o'zgarmas qiymat",
                'verbose_name_plural': "Vagon Qarshili uchun o'zgarmas qiymatlar",
            },
        ),
    ]
