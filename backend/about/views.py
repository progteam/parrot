"""
backend/about/views.py

Views for the about page
- progteam_desc
- meeting_info
- officer_info
"""
from django.http import JsonResponse
from .models import MeetingInfo, OfficerInfo, ProgteamDesc


def meeting_info(request):
    """backend.about.urls: /about/meeting-info

    Meeting Information
    TODO: We're returning all the meeting information. This requires admins
    edit existing meetings (or delete the old ones). An alternative way is to
    filter the meeting info by the current academic term.
    """
    fmt = '%I:%M %p'
    meetings = map(
        lambda obj: {
            'dayOfWeek': obj.day_of_week,
            'room': obj.room,
            'term': obj.term,
            'timeStart': obj.time_start.strftime(fmt),
            'timeEnd': obj.time_end.strftime(fmt),
        }, MeetingInfo.objects.all())
    return JsonResponse(list(meetings), safe=False)


def officer_info(request):
    """backend.about.urls: /about/officer-info

    Officer Information
    TODO: Similar to the TODO item in backend.about.views.meeting_info
    """
    officers = map(
        lambda obj: {
            'email': obj.email,
            'name': obj.name,
            'profileImg': obj.profile_img,
            'role': obj.role,
            'term': obj.term,
        }, OfficerInfo.objects.all())
    return JsonResponse(list(officers), safe=False)


def progteam_desc(request):
    """backend.about.urls: /about/progteam-desc

    Progteam team description. We assume there is only one description object
    lives in the table, and returns the first and only one.
    """
    obj = ProgteamDesc.objects.first()
    return JsonResponse({
        'desc': obj.desc,
    })
