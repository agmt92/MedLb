from django.db import models

class MedsDrug(models.Model):
    code = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subsidy = models.DecimalField(max_digits=10, decimal_places=2)
    excdate = models.DateField()
    country = models.ForeignKey('MedsCountry', on_delete=models.DO_NOTHING, db_column='country_id', related_name='drugs')
    manufacturer = models.ForeignKey('MedsManufacturer', on_delete=models.DO_NOTHING, db_column='manufacturer_id', related_name='drugs')
    agent = models.ForeignKey('MedsAgent', on_delete=models.DO_NOTHING, db_column='agent_id', related_name='drugs')
    presentation = models.ForeignKey('MedsPresentation', on_delete=models.DO_NOTHING, db_column='presentation_id', related_name='drugs')
    bg = models.ForeignKey('MedsBg', on_delete=models.DO_NOTHING, db_column='bg_id', related_name='drugs')
    ingredient = models.ForeignKey('MedsIngredient', on_delete=models.DO_NOTHING, db_column='ingredient_id', related_name='drugs')
    name = models.ForeignKey('MedsName', on_delete=models.DO_NOTHING, db_column='name_id', related_name='drugs')
    form = models.ForeignKey('MedsForm', on_delete=models.DO_NOTHING, db_column='form_id', related_name='drugs')
    dosage = models.ForeignKey('MedsDosage', on_delete=models.DO_NOTHING, db_column='dosage_id', related_name='drugs')
    atc = models.ForeignKey('MedsAtc', on_delete=models.DO_NOTHING, db_column='atc_id', related_name='drugs')
    resparty = models.ForeignKey('MedsResparty', on_delete=models.DO_NOTHING, db_column='resparty_id', related_name='drugs')
    rescountry = models.ForeignKey('MedsRescountry', on_delete=models.DO_NOTHING, db_column='rescountry_id', related_name='drugs')
    regnum = models.ForeignKey('MedsRegnum', on_delete=models.DO_NOTHING, db_column='regnum_id', related_name='drugs')
    strength = models.ForeignKey('MedsStrength', on_delete=models.DO_NOTHING, db_column='strength_id', related_name='drugs')
    subsidy_rel = models.ForeignKey('MedsSubsidy', on_delete=models.DO_NOTHING, db_column='subsidy_id', related_name='drugs')

    class Meta:
        managed = False
        db_table = 'meds_drug'

class MedsAgent(models.Model):
    agenam = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'meds_agent'

class MedsAtc(models.Model):
    atcnam = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'meds_atc'

class MedsBg(models.Model):
    bgnam = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'meds_bg'

class MedsCountry(models.Model):
    counam = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'meds_country'

class MedsDosage(models.Model):
    dosnam = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'meds_dosage'

class MedsForm(models.Model):
    formnam = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'meds_form'

class MedsIngredient(models.Model):
    ingnam = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'meds_ingredient'

class MedsManufacturer(models.Model):
    mannam = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'meds_manufacturer'

class MedsName(models.Model):
    namnam = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'meds_name'

class MedsPresentation(models.Model):
    presnam = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'meds_presentation'

class MedsRegnum(models.Model):
    regnam = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'meds_regnum'

class MedsResparty(models.Model):
    resparnam = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'meds_resparty'

class MedsRescountry(models.Model):
    rescounam = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'meds_rescountry'

class MedsStrength(models.Model):
    strenam = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'meds_strength'

class MedsSubsidy(models.Model):
    subnam = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'meds_subsidy'
