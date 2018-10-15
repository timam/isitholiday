from django.http import HttpResponse
from .models import Entry
import datetime

# Create your views here.

gimme_date = datetime.datetime.now().date()
entry = Entry.objects.filter(date__exact=gimme_date).get()
status = entry.status


def index(request):

    return HttpResponse(status)

