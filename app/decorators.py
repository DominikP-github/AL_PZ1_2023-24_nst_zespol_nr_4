# decorators.py
from functools import wraps
from django.shortcuts import redirect

def has_special_group_permission(user):
    return user.groups.filter(name='SpecialGroup').exists()

def special_group_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if has_special_group_permission(request.user):
            return redirect('special_page')
        else:
            return view_func(request, *args, **kwargs)

    return _wrapped_view
