from django.db import models
from django.conf import settings


class Atc(models.Model):
    atcnam = models.CharField(max_length=255, unique=True, null=True)  # This stays NOT NULL

class Atc1(models.Model):
    atc1nam = models.CharField(max_length=255, unique=True, null=True)
    atc1desc = models.CharField(max_length=255, unique=True, null=True)

class Atc2(models.Model):
    atc2nam = models.CharField(max_length=255, unique=True, null=True)
    atc2desc = models.CharField(max_length=255, unique=True, null=True)


class Atc3(models.Model):
    atc3nam = models.CharField(max_length=255, unique=True, null=True)
    atc3desc = models.CharField(max_length=255, unique=True, null=True)


class Atc4(models.Model):
    atc4nam = models.CharField(max_length=255, unique=True, null=True)
    atc4desc = models.CharField(max_length=255, unique=True, null=True)

class Bg(models.Model):
    bgnam = models.CharField(max_length=255, unique=True, null=True)

class Dosage(models.Model):
    dosnam = models.CharField(max_length=255, unique=True, null=True)

class Presentation(models.Model):
    presnam = models.CharField(max_length=255, unique=True, null=True)

class Form(models.Model):
    formnam = models.CharField(max_length=255, unique=True, null=True)

class Agent(models.Model):
    agenam = models.CharField(max_length=255, unique=True, null=True)

class ExDate(models.Model):
    exdnam = models.CharField(max_length=255, unique=True, null=True)

class Country(models.Model):
    counam = models.CharField(max_length=255, unique=True, null=True)

class Manufacturer(models.Model):
    mannam = models.CharField(max_length=255, unique=True, null=True)

class Ingredient(models.Model):
    ingnam = models.CharField(max_length=255, unique=True, null=True)

class Regnum(models.Model):
    regnam = models.CharField(max_length=255, unique=True, null=True)


class Strength(models.Model):
    strenam = models.CharField(max_length=255, unique=True, null=True)

class Subsidy(models.Model):
    subnam = models.CharField(max_length=255, unique=True, null=True)

class Name(models.Model):
    namnam = models.CharField(max_length=255, unique=True, null=True)

class Resparty(models.Model):
    resparnam = models.CharField(max_length=255, unique=True, null=True)

class Rescountry(models.Model):
    rescounam = models.CharField(max_length=255, unique=True, null=True)


class Drug(models.Model):
    subnam = models.ForeignKey(Subsidy, on_delete=models.CASCADE, null=True)
    excdate = models.ForeignKey(ExDate, on_delete=models.CASCADE, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True)
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE, null=True)
    code = models.IntegerField(null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(null=True)
    price17424 = models.IntegerField(null=True)
    bg = models.ForeignKey(Bg, on_delete=models.CASCADE, null=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True)
    name = models.ForeignKey(Name, on_delete=models.CASCADE, null=True)
    form = models.ForeignKey(Form, on_delete=models.CASCADE, null=True)
    dosage = models.ForeignKey(Dosage, on_delete=models.CASCADE, null=True)

    atc = models.ForeignKey(Atc, on_delete=models.CASCADE, null=True)
    atc1 = models.ForeignKey(Atc1, on_delete=models.CASCADE, null=True)
    atc2 = models.ForeignKey(Atc2, on_delete=models.CASCADE, null=True)
    atc3 = models.ForeignKey(Atc3, on_delete=models.CASCADE, null=True)
    atc4 = models.ForeignKey(Atc4, on_delete=models.CASCADE, null=True)

    resparty = models.ForeignKey(Resparty, on_delete=models.CASCADE, null=True)
    rescountry = models.ForeignKey(Rescountry, on_delete=models.CASCADE, null=True)
    regnum = models.ForeignKey(Regnum, on_delete=models.CASCADE, null=True)

    #Favs
    favorites = models.ManyToManyField(settings.AUTH_USER_MODEL,
        through='FavMed', related_name='favorite_med')
    # Shows up in the admin list
    def __str__(self):
        return self.name

class FavMed(models.Model) :
    med = models.ForeignKey(Drug, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favs_users')

    # https://docs.djangoproject.com/en/4.2/ref/models/options/#unique-together
    class Meta:
        unique_together = ('med', 'user')

    def __str__(self) :
        return '%s likes %s'%(self.user.username, self.drug.id[:10])

