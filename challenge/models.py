from datetime import datetime, timedelta
from django.db import models

class Status(models.Model):
   # Status of the challenge.
   name = models.CharField('Status', max_length = 100)

   class Meta:
      verbose_name_plural = "Statuses"

   def __unicode__(self):
      return self.name

class Challenge(models.Model):
   title = models.CharField('Challenge Title', max_length = 200)
   starts = models.DateTimeField('Start Date', default = datetime.now)
   ends = models.DateTimeField('End Date', default = lambda: datetime.now() + timedelta(days=7))
   status = models.ForeignKey(Status)
   summary = models.TextField('Challenge Details')

   def __unicode__(self):
      return self.title

