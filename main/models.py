from django.db import models


class Bolim(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Taom(models.Model):
    nom = models.CharField(max_length=100)
    narx = models.IntegerField()

    def __str__(self):
        return self.nom


class Stol(models.Model):
    raqam = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.raqam


class Buyurtma(models.Model):
    izoh = models.TextField(blank=True, null=True)
    sana = models.DateTimeField(auto_now_add=True)
    hisoblandi = models.FloatField(default=0)
    tolandi = models.BooleanField(default=False)

    def __str__(self):
        return self.izoh


class BTaom(models.Model):
    buyurtma = models.ForeignKey(Buyurtma, on_delete=models.CASCADE)
    taom = models.ForeignKey(Taom, on_delete=models.CASCADE)
    miqdor = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.buyurtma.__str__() + self.taom.__str__()

    def save(self, *args, **kwargs):
        self.buyurtma.hisoblandi += self.taom.narx * self.miqdor
        self.buyurtma.save()
        super().save(*args, **kwargs)

