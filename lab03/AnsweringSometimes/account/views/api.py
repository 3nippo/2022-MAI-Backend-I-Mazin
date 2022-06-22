from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from account.models import User, UserSerializer
from django.db.models import Count, F
from django.core.files.storage import FileSystemStorage

@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def account_data(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAdminUser])
def specific_account_data(request, pk):
    try:
        serializer = UserSerializer(User.objects.get(id=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAdminUser])
def age_bars(request):
    age_bars = User.objects.values('age').annotate(count=Count('age')).order_by('-count', 'age')
    
    return Response(age_bars, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAdminUser])
def gender_bars(request):
    gender_bars = User.objects.values('gender').annotate(count=Count('gender')).order_by('-count', 'gender')
    
    return Response(gender_bars, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def upload_avatar(request):
    if len(request.FILES) != 1:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    request_file, = request.FILES.values()

    request.user.avatar = request_file
    request.user.save()

    f = request.user.avatar
    
    try:
        path = f.path
    except NotImplementedError:
        path = 'Not supported'

    return Response({
        'url': f.url,
        'path': path,
    }, status=status.HTTP_200_OK)


# returns 'items_size' latest items from search history
#   skipping first 'items_size * items_idx'
#   note: items might be updated between requests
def search_history(request, items_size=10, items_idx=0):
    return JsonResponse({
        'items': [
            {
                'question': 'how to google?',
                'results_num': 1,
                'searched_num': 10,
                'clicked_results': 0,
                'request_link': '/dev/null'
            }
        ]
    })
