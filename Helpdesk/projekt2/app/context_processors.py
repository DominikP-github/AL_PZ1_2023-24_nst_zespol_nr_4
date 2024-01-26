# myapp/context_processors.py

from .models import SearchHistory

def search_history(request):
    user_search_history = []
    
    if request.user.is_authenticated:
        user_search_history = SearchHistory.objects.filter(user=request.user).order_by('-timestamp')[:5]
    
    return {'user_search_history': user_search_history}
