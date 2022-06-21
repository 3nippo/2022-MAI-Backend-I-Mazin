from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from search_backend.models import SearchItem, History
from django.db.models import Sum, F

@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAdminUser])
def top_n_searched(request, n):
    result = History.objects.values(question=F('item__question')).annotate(clicks=Sum('results_clicks_num')).order_by('-clicks')[:n]

    return Response(result, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAdminUser])
def top_n_marketed(request, n):
    result = History.objects.values(question=F('item__question')).annotate(clicks=Sum('marketing_clicks_num')).order_by('-clicks')[:n]

    return Response(result, status=status.HTTP_200_OK)
