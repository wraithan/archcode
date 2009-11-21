from django.db import models

class Status(models.Model):
   # Status of the contest.
   name = models.CharField('Status', max_length = 100)

   def __unicode__(self):
      return self.name

class Contest(models.Model):
   title = models.CharField('Contest Title', max_length = 200)
   starts = models.DateTimeField('Start Date', auto_now = True, auto_now_add = True)
   ends = models.DateTimeField('End Date', auto_now = True, auto_now_add = True)
   status = models.ForeignKey(Status)
   summary = models.TextField('Contest Details')

   def __unicode__(self):
      return self.title

