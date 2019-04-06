"""
backend/events/models.py

Events Page Data Models
- Event
- Team
- TeamMember

An event could have many teams if the event is a coding competition. Each team
would have many team members, and each team member could have many teams as
well (i.e. a constant competed in different contests).
"""
from django.contrib import admin
from django.db import models


class Event(models.Model):
    """The event model

    An event could be a coding competition which has many teams and final
    standings (scoreboards); or a general event which would not have teams (but
    it would have a description instead). We allow HTML for the description.
    """
    date = models.DateField()
    desc = models.TextField(blank=True)
    div1_scoreboard = models.URLField(blank=True)
    div2_scoreboard = models.URLField(blank=True)
    img_url = models.URLField()
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def teams(self):
        """Teams associated with this event
        """
        return Team.objects.filter(event=self)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    """Data model for a team member
    A team member could have many teams if competed in many competitions
    """
    name = models.CharField(max_length=256)
    profile_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    """Data model for a team
    A team has
    - division: none, div1 or div2
    - event: the competition
    - members: the contestants in this team
    - name: the team name
    - rank: the relative ranking within its division
    """
    division = models.CharField(
        max_length=1,
        choices=(
            ('1', 'DIV 1'),
            ('2', 'DIV 2'),
        ),
        blank=True,
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    members = models.ManyToManyField(TeamMember)
    name = models.CharField(max_length=256)
    rank = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Allow admins to edit the data models
admin.site.register(Event)
admin.site.register(Team)
admin.site.register(TeamMember)
