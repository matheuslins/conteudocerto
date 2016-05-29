from django.shortcuts import render
from .forms import *

def home(request):
    contexto = {}
    if request.method == "POST":
        form = Contact(request.POST)
        if form.is_valid():
            contexto['is_valid'] = True
            email = Mailing.create(form.cleaned_data['email'])
            email.save()
            form.send_mail()
            form = Contact()
    else:
        form = Contact()
    contexto['form'] = form
    template_name = 'index.html'
    return render(request, template_name, contexto)