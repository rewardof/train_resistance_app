from django.contrib.postgres.fields import ArrayField
from django.db import models


class Locomotiv(models.Model):
    TYPE_LOCOMOTIV = (
        (1, "Manyovr Lokomotivi"),
        (2, "Poyezd Lokomotivi")
    )
    locomotiv_name = models.CharField("Lokomotiv nomi", max_length=32)
    locomotiv_seria = models.CharField("Lokomotiv seriyasi", max_length=32)
    locomotiv_number = models.CharField("Lokomotiv raqami", max_length=32)
    type_locomotiv = models.IntegerField("Lokomotiv turi", choices=TYPE_LOCOMOTIV)
    value_ao = models.FloatField("ao qiymati")
    value_bo = models.FloatField("bo qiymati")
    value_co = models.FloatField("co qiymati")
    value_aox = models.FloatField("aox qiymati")
    value_box = models.FloatField("box qiymati")
    value_cox = models.FloatField("cox qiymati")
    is_active = models.BooleanField("Faol", default=True)
    created_at = models.DateTimeField("Yaratilgan vaqt", auto_now_add=True)
    updated_at = models.DateTimeField("Tahrirlangan vaqt", auto_now=True)

    class Meta:
        verbose_name = "Lokomotiv Turi"
        verbose_name_plural = "Lokomotiv Turlari"

    def __str__(self):
        return f"{self.locomotiv_name}, {self.locomotiv_seria}-{self.locomotiv_number}"


class TotalDataVagon(models.Model):
    number_vagon = models.IntegerField("Vagon raqami")
    number_of_arrow = models.SmallIntegerField("O'qlar soni")
    netto_vagon = models.FloatField("Vagon og'irligi")
    length_vagon = models.FloatField("Vagon uzunligi")
    total_weight = models.FloatField("Umumiy og'irlik")
    bullet_weight = models.FloatField("O'qqa tushadigan og'irlik")

    def __str__(self):
        return f"{self.number_vagon}-raqamli vagon xarakteristikasi"

    class Meta:
        verbose_name = "Vagon xarakteristikasi"
        verbose_name_plural = "Vagonlar xarakteristikasi"


class VagonResistanceConstant(models.Model):
    value_ao = models.FloatField("ao qiymati")
    value_bo = models.FloatField("bo qiymati")
    value_co = models.FloatField("co qiymati")
    value_aox = models.FloatField("aox qiymati")
    value_box = models.FloatField("cox qiymati")
    value_cox = models.FloatField("cox qiymati")
    value_ax = models.FloatField("ax qiymati")
    value_bx = models.FloatField("bx qiymati")
    value_cx = models.FloatField("cx qiymati")

    class Meta:
        verbose_name = "Vagon Qarshili uchun o'zgarmas qiymat"
        verbose_name_plural = "Vagon Qarshili uchun o'zgarmas qiymatlar"


class Excel(models.Model):
    file = models.FileField("Excel file", upload_to='files/')

    class Meta:
        verbose_name = 'Excel file'
        verbose_name_plural = 'Excel filelar'

