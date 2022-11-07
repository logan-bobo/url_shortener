from django.shortcuts import HttpResponse, HttpResponseRedirect, get_object_or_404
from .models import Link


def index(request):
    return HttpResponse('THIS IS THE MAIN PAGE')


def redirect(request, uuid: str):
    row = get_object_or_404(Link, uuid=uuid)
    return HttpResponseRedirect(f'https://{row.origin_link}')
