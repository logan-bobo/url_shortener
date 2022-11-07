from django.shortcuts import HttpResponse, HttpResponseRedirect, get_object_or_404, render
from django.template import loader
from .models import Link


def index(request):
    return render(request, 'shortening_service/index.html')


def redirect(request, uuid: str):
    row = get_object_or_404(Link, uuid=uuid)
    return HttpResponseRedirect(f'https://{row.origin_link}')
