from django.db.models import *
from base.models import Profiel
from livefield.models import *
from datetime import datetime
from django.template import loader

class Courant(LiveModel):
  publish_date = DateTimeField(blank=True, null=True)
  date_created = DateTimeField(default=datetime.now)
  date_modified = DateTimeField(default=datetime.now)
  template = CharField(max_length=50)
  user = ForeignKey(Profiel)

  def render(self):
    return loader.render_to_string(self.template, context={
      'publish_date': self.publish_date,
      'date_created': self.date_created,
      'date_modified': self.date_modified,
      'user': self.user,
      'entries': self.entries.all()
    })

  def __str__(self):
    if self.publish_date is None:
      return "Courant without a publish date"
    elif self.publish_date >= datetime.now():
      return "Courant published on %s" % self.publish_date
    else:
      return "Courant scheduled for %s" % self.publish_date

class CourantEntry(LiveModel):
  courant = ForeignKey(Courant, related_name='entries')
  title = CharField(max_length=100)
  category = CharField(max_length=9)
  text = TextField()
  order = IntegerField(default=0)
  user = ForeignKey(Profiel)
  date_created = DateTimeField(default=datetime.now)
  date_modified = DateTimeField(default=datetime.now)

  class Meta:
    ordering = ['order', 'pk']

  def __str__(self):
    return self.title
