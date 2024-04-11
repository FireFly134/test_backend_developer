from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=100, verbose_name="Наименование",)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "наименование меню"
        verbose_name_plural = "Наименования меню"


class MenuItem(models.Model):
    title = models.CharField(max_length=100, verbose_name="Наименование",)
    parent = models.ForeignKey(
        Menu,
        verbose_name="Наименование меню",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "наименование товара"
        verbose_name_plural = "Наименования товарво"