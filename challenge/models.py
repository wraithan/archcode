from datetime import datetime, timedelta
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

CHALLENGE_STATUS_CHOICES = (
    ('NW', 'New'),
    ('IP', 'In Progress'),
    ('CP', 'Completed'),
)

class Challenge(models.Model):
    title = models.CharField('Challenge Title', max_length = 200)
    starts = models.DateTimeField('Start Date', default = datetime.now)
    ends = models.DateTimeField('End Date', default = lambda: datetime.now() +
        timedelta(days=7))
    status = models.CharField('Challenge Status', max_length = 2,
        choices=CHALLENGE_STATUS_CHOICES)
    summary = models.TextField('Challenge Details')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('challenge-details', args=[self.id,])

class Language(models.Model):
    name = models.CharField('Language Name', max_length = 30)

    def __unicode__(self):
        return self.name

class Solution(models.Model):
    language = models.ForeignKey(Language)
    source = models.TextField('Solution Source')
    challenge = models.ForeignKey(Challenge)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user.username + ": " + self.challenge.title
