from models import note
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    items = note.objects.all()
    return render_to_response('base.html', {'items': items})
