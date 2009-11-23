from datetime import datetime, timedelta
from django.db import models

class Status(models.Model):
   # Status of the contest.
   name = models.CharField('Status', max_length = 100)

   class Meta:
      verbose_name_plural = "Statuses"

   def __unicode__(self):
      return self.name

class Contest(models.Model):
   title = models.CharField('Contest Title', max_length = 200)
   starts = models.DateTimeField('Start Date', default = datetime.now)
   ends = models.DateTimeField('End Date', default = lambda: datetime.now() + timedelta(days=7))
   status = models.ForeignKey(Status)
   summary = models.TextField('Contest Details')

   def __unicode__(self):
      return self.title

