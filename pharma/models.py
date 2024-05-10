from django.db import models
from django.conf import settings


class Mouhafaza(models.Model):
    mounam = models.CharField(max_length=255, unique=True, null=True)

class Casa(models.Model):
    casnam = models.CharField(max_length=255, unique=True, null=True)
    mouhafaza = models.ForeignKey(Mouhafaza, on_delete=models.CASCADE, null=True)

class Address(models.Model):
    addnam = models.CharField(max_length=255, unique=True, null=True)
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE, null=True)

class Phones(models.Model):
    phonam = models.CharField(max_length=255, unique=True, null=True)

class Pharmain(models.Model):

    phanam = models.CharField(max_length=255, unique=True, null=True)
    phacistnam = models.CharField(max_length=255, unique=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    phones = models.ForeignKey(Phones, on_delete=models.CASCADE, null=True)

class FavoritePharmacy(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pharmacy = models.ForeignKey(Pharmain, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'pharmacy')

    def __str__(self):
        return f"{self.user.username} favorites {self.pharmacy.phanam}"