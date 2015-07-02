from django.db.models import *
from base.models import Profiel
from livefield import LiveModel
from datetime import datetime, time

class MaaltijdRepetitie(Model):
  id = AutoField(primary_key=True, db_column='mlt_repetitie_id')
  dag_vd_week = IntegerField()
  periode_in_dagen = IntegerField()
  standaard_titel = CharField(max_length=255)
  standaard_tijd = TimeField(default=time(hour=18))
  standaard_prijs = IntegerField(default=3)
  abonneerbaar = IntegerField()
  standaard_limiet = IntegerField(default=100)
  abonnement_filter = CharField(max_length=255, blank=True)

  def __str__(self):
    return "Repetitie: %s" % self.standaard_titel

  class Meta:
    db_table = 'mlt_repetities'

class Maaltijd(LiveModel):
  # fields
  id = AutoField(primary_key=True, db_column="maaltijd_id")
  repetitie = ForeignKey(MaaltijdRepetitie, blank=True, null=True, db_column="mlt_repetitie_id")
  titel = CharField(max_length=255)
  datum = DateField()
  tijd = TimeField(default=time(hour=18))
  prijs = IntegerField(default=3)
  omschrijving = CharField(max_length=255, blank=True)

  gesloten = BooleanField(default=False)
  laatst_gesloten = DateTimeField(blank=True, null=True)

  aanmeld_filter = CharField(max_length=255, blank=True) # permissions specifier
  aanmeld_limiet = IntegerField(default=100)

  def __str__(self):
    return "Maaltijd: %s" % self.titel

  class Meta:
    db_table = 'mlt_maaltijden'

class MaaltijdAanmelding(Model):
  maaltijd = ForeignKey(Maaltijd, related_name="aanmeldingen")
  user = ForeignKey(Profiel, db_column='uid')
  aantal_gasten = IntegerField()
  gasten_eetwens = CharField(max_length=255, blank=True)

  door_abonnement = ForeignKey(MaaltijdRepetitie, db_column='door_abonnement', blank=True, null=True)
  door_user = ForeignKey(Profiel, null=True, db_column='door_uid', related_name='+')
  laatst_gewijzigd = DateTimeField()

  def __str__(self):
    return "Aanmelding: lid %s bij %s" % (self.user_id, self.maaltijd_id)

  class Meta:
    unique_together = (('maaltijd', 'user'),)
    db_table = 'mlt_aanmeldingen'

class MaaltijdAbo(Model):
  repetitie = ForeignKey(MaaltijdRepetitie, db_column="mlt_repetitie_id")
  user = ForeignKey(Profiel, db_column='uid')
  wanneer_ingeschakeld = DateTimeField()

  def __str__(self):
    return "Abo voor lid %s bij repetitie %s" % (self.user_id, self.repetitie_id)
  class Meta:
    unique_together = (('user', 'repetitie'))
    db_table = 'mlt_abonnementen'
