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
    value_ao = models.DecimalField("ao qiymati", max_digits=10, decimal_places=5)
    value_bo = models.DecimalField("bo qiymati", max_digits=10, decimal_places=5)
    value_co = models.DecimalField("co qiymati", max_digits=10, decimal_places=5)
    value_aox = models.DecimalField("aox qiymati", max_digits=10, decimal_places=5)
    value_box = models.DecimalField("box qiymati", max_digits=10, decimal_places=5)
    value_cox = models.DecimalField("cox qiymati", max_digits=10, decimal_places=5)
    is_active = models.BooleanField("Faol", default=True)
    created_at = models.DateTimeField("Yaratilgan vaqt", auto_now_add=True)
    updated_at = models.DateTimeField("Tahrirlangan vaqt", auto_now=True)

    class Meta:
        verbose_name = "Lokomotiv Turi"
        verbose_name_plural = "Lokomotiv Turlari"

    def __str__(self):
        return f"{self.locomotiv_name}, {self.locomotiv_seria}-{self.locomotiv_number}"
