from datetime import datetime, timedelta
from django.db import models

CHALLENGE_STATUS_CHOICES = (
    ('NW', 'New'),
    ('IP', 'In Progress'),
    ('CP', 'Completed'),
)

class Challenge(models.Model):
    title = models.CharField('Challenge Title', max_length = 200)
    starts = models.DateTimeField('Start Date', default = datetime.now)
    ends = models.DateTimeField('End Date', default = lambda: datetime.now() + timedelta(days=7))
    status = models.CharField('Challenge Status', max_length = 2, choices=CHALLENGE_STATUS_CHOICES)
    summary = models.TextField('Challenge Details')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/challenge/%i/" % self.id

