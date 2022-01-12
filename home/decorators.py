from django.http import HttpResponse


def have_orgization():
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            try:
                if request.user.organization == None:
                    return func(request, *args, **kwargs)
                else:
                    return HttpResponse('User already have organization', status=401)
            except Exception as e:
                return HttpResponse(e, status=401)
        return wrapper
    return decorator


def admin_access_check():
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            try:
                if request.user.organization_permission == '9':
                    return func(request, *args, **kwargs)
                else:
                    return HttpResponse('User is unauthorized', status=401)
            except Exception as e:
                return HttpResponse(e, status=401)
        return wrapper
    return decorator
