from .models import Historia

def search_history(request):
    user_search_history = []
    
    if request.user.is_authenticated:
        user_search_history = Historia.objects.filter(user=request.user).order_by('-czas')[:5]
    
    return {'user_search_history': user_search_history}
