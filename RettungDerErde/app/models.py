"""
Definition of models.
"""

from django.db import models
from django.db.models import Sum


class Poll(models.Model):
    """A poll object for use in the application views and repository."""
    text = models.CharField('Netzwerk',max_length=200)
    Status = models.BooleanField(default = 0)
    geplanter_Status = models.BooleanField(default = 0)
    pub_date = models.BooleanField('Status')
    Kurzbeschreibung = models.CharField(max_length=200, default='')

    def total_Satus(self):
        """Calculates the total number of votes for this poll."""
        return self.choice_set.aggregate(Sum('Status'))['Status__sum']

    def __unicode__(self):
        """Returns a string representation of a poll."""
        return self.text


class Choice(models.Model):
    """A poll choice object for use in the application views and repository."""
    poll = models.ForeignKey(Poll, on_delete = models.CASCADE)
    text = models.CharField(max_length=200)
    Status = models.BooleanField()
    

  
    def __unicode__(self):
        """Returns a string representation of a choice."""
        return self.text