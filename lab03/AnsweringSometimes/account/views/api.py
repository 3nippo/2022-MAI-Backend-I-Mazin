from django.http import JsonResponse

def account_data(request):
    return JsonResponse({
        'name': 'John',
        'last_name': 'Snow'
    })

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
