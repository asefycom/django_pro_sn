from django.http import HttpResponseBadRequest

def ajax_required(f):
    def wrap(request, *args, **kwargs):
        # if not request.is_ajax():
        if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
            print("Bad Request")
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)
    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap