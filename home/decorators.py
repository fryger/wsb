from django.http import HttpResponse


def is_org_admin_or_unauthorized():
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            if request.user.profile.org.admin == request.user:
                return func(request, *args, **kwargs)
            else:
                return HttpResponse('Unauthorized', status=401)
        return wrapper
    return decorator
