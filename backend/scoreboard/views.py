"""
backend/scoreboard/views.py

Views for the scoreboard page

"""
from datetime import datetime, timedelta
from django.utils.timezone import get_current_timezone
from django.http import JsonResponse
from django.db.models import Max, Min
from .models import KattisScore

def scores_week(request):
    """
    Returns the score difference for each KattisHandle
    for the past week.
    """
    week_ago = datetime.now(
        tz=get_current_timezone()) - timedelta(days=7)
    query_result = KattisScore.objects.filter(
        created_at__gte=week_ago
    ).values('kattis_handle__handle').annotate(
        points=Max('score') - Min('score')
    )
    score_diff_list = map(
        lambda obj: {
            "username" : obj['kattis_handle__handle'],
            "points" : obj['points'],
        }, query_result)
    return JsonResponse(list(score_diff_list), safe=False)
