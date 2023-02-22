from django.contrib.postgres.fields import ArrayField
from django.db import models
from utils.constants import CONSTANTS


class Locomotiv(models.Model):
    TYPE_LOCOMOTIV = (
        (1, "Manyovr Lokomotivi"),
        (2, "Poyezd Lokomotivi")
    )
    locomotiv_name = models.CharField("Lokomotiv nomi", max_length=32)
    locomotiv_seria = models.CharField("Lokomotiv seriyasi", max_length=32)
    locomotiv_number = models.CharField("Lokomotiv raqami", max_length=32)
    weigth = models.FloatField("Lokomotiv og'irligi")
    lenght = models.FloatField("Lokomotiv uzunligi")
    number_arrows = models.SmallIntegerField("O'qlar soni")
    type_locomotiv = models.IntegerField("Lokomotiv turi", choices=TYPE_LOCOMOTIV)
    force_per_arrow = models.FloatField("Bitta o‘qga bosilishidagi haqiqiy kuchi")
    force_all_arrows = models.FloatField("Barcha o‘qga bosilishidagi haqiqiy kuchi")
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
    vagon_type = models.CharField(choices=CONSTANTS.VAGON_TYPE.CHOICES, max_length=8, null=True)
    load_weight = models.FloatField("Yuk og'irligi")
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


class TrainResistanceData(models.Model):
    capacity = models.IntegerField()
    locomotiv_traction_mode = models.FloatField()
    locomotiv_idle_mode = models.FloatField()
    total_resistance_vagon = models.FloatField()
    total_resistance_traction = models.FloatField()
    total_resistance_idle = models.FloatField()
    outside_temperature_resistance = models.FloatField()
    wind_capacity_resistance = models.FloatField()
    resistance_vagon_ahead = models.FloatField()
    railroad_condition_resistance = models.FloatField()
    all_traction_resistance = models.FloatField()
    specific_traction_resistance = models.FloatField()
    all_idle_resistance = models.FloatField()
    specific_idle_resistance = models.FloatField()
    declivity_resistance = models.FloatField()
    curvature_resistance = models.FloatField()
    switch_curvature_resistance = models.FloatField()


class RailwaySwitchMark(models.Model):
    title = models.CharField("Nomi", max_length=128, blank=True)
    mark = models.CharField("Markasi", max_length=16)
    a = models.FloatField("a masofasi uzunligi")
    b = models.FloatField("b masofasi uzunligi")
    rail_type = models.CharField("Rels turi", max_length=16, blank=True, null=True)
    radius = models.IntegerField("Egrilik radiusi")
    length_curvature = models.IntegerField("Egrilik uzunligi")

    class Meta:
        verbose_name = "Stelkali o'tkazgich markasi"
        verbose_name_plural = "Strelkali o'tkazgichlar markalari"

    def __str__(self):
        return self.mark


class RailRoadCharacteristic(models.Model):
    title = models.CharField(max_length=256)
    coefficient = models.FloatField()

    class Meta:
        verbose_name = "Yo'l xarakteristikasi"
        verbose_name_plural = "Yo'l xarakteristikasi"

    def __str__(self):
        return self.title


class WeightModel(models.Model):
    locomotiv_weight = models.FloatField()
    vagons_weight = models.FloatField()
    locomotiv = models.ForeignKey(Locomotiv, on_delete=models.CASCADE)
