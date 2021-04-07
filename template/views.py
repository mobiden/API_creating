from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def template_echo(request):
    if 'X-Print-Statement' in request.headers:
        return HttpResponse(content='statement is test', status=200)

    par = request.GET.keys()
    str1 = request.GET.dict()
    st = str(str1).strip('{').strip('}').split('\'')
    stri = ''.join(st)
    reqme = '' if stri == '' else str(request.method).lower()


    content = reqme +' ' + stri + ' statement is empty'

    return HttpResponse(content=content, status=200)