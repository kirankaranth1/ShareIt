# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from myproject.myapp.forms import EmailForm
from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            url=newdoc.docfile.url
            request.session['file_url'] = url

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.email_url'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'myapp/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def send_url(email,name,url):
     #Need to put mail function here
     #send_mail('Subject here', 'Here is the message.', 'messanger@localhost.com',['any@email.com'], fail_silently=False)
    print("Sharing %s with %s as %s" %(url,email,name))



def email_url(request):
    file_url = request.session.get('file_url')
    hostname = request.get_host()
    file_url = str(hostname) + str(file_url)
    eform = EmailForm(request.POST or None)
    if eform.is_valid():
        email = eform.cleaned_data["email"]
        name = eform.cleaned_data["name"]
        send_url(email,name,file_url)
        request.session['recipentEmail'] = email
        request.session['name'] = name
        request.session['file_url'] = file_url
        return HttpResponseRedirect(reverse('myproject.myapp.views.thank_you'))
    context = { "eform": eform, "file_url":file_url,}
    return render(request,"myapp/email_share.html",context)

def thank_you(request):
    recipentEmail = request.session.get('recipentEmail')
    recipentName = request.session.get('name')
    file_url = request.session.get('file_url')
    context = { "recipentName": recipentName,"recipentEmail": recipentEmail, "file_url":file_url}
    return render(request,"myapp/thank_you.html",context)