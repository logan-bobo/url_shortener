from django.shortcuts import (
    HttpResponse,
    HttpResponseRedirect,
    get_object_or_404,
    render
)
from .models import Link


def index(request):
    return render(request, 'shortening_service/index.html')


def generate_link(request):
    pass


def redirect(request, generated_id: str):
    row = get_object_or_404(Link, generated_id=generated_id)
    return HttpResponseRedirect(f'https://{row.origin_link}')
