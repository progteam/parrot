"""
backend/events/views.py

Views for the events page
"""
from django.http import JsonResponse
from .models import Event


def encode_member(member):
    """Encode a team member and return fields:
    - name
    - profileUrl (optional)
    """
    res = {
        'name': member.name,
    }
    if member.profile_url:
        res['profileUrl'] = member.profile_url
    return res


def encode_team(team):
    """Encode a team and return its fields
    """
    return {
        'division': team.division,
        'members': list(map(encode_member, team.members.all())),
        'name': team.name,
        'rank': team.rank,
    }


def encode_event(event):
    """Encode an event and return fields:
    - date
    - desc (optional)
    - div1Scoreboard (optional)
    - div2Scoreboard (optional)
    - imgUrl
    - name
    - teams (optional)
    """
    fmt = '%m/%d/%Y'
    res = {
        'date': event.date.strftime(fmt),
        'imgUrl': event.img_url,
        'name': event.name,
    }
    if event.desc:
        res['desc'] = event.desc
    if event.div1_scoreboard:
        res['div1Scoreboard'] = event.div1_scoreboard
    if event.div2_scoreboard:
        res['div2Scoreboard'] = event.div2_scoreboard
    teams = event.teams().all()
    if teams:
        res['teams'] = list(map(encode_team, teams))
    return res


def events_data(request):
    """Encode all events as a Json response
    """
    events = map(encode_event, Event.objects.all())
    return JsonResponse(list(events), safe=False)
