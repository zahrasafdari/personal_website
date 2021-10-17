from django.shortcuts import render

from zs_contact.models import ContactUs
from django.shortcuts import render
from .forms import CreateContactForm


# Create your views here.


def contact_page(request):


    return render(request, 'home_page.html', context)