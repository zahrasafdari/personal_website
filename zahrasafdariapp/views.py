from zs_contact.forms import CreateContactForm
from zs_contact.models import ContactUs
from django.shortcuts import render, redirect


def home_page(request):

    context = {
    }
    contact_form = CreateContactForm(request.POST or None)

    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')
        ContactUs.objects.create(fullname=full_name, email=email, subject=subject, text=text, is_read=False)
        # todo : show user a success message
        contact_form = CreateContactForm()
    context = {
        'contact_form': contact_form,
    }
    return render(request, 'home_page.html', context)