from django.shortcuts import render
from django.http import HttpResponse
from forms import CommentForm,PostForm,ContactForm
from django.core.mail import BadHeaderError, send_mail
from django.contrib.auth.decorators import login_required

@login_required(login_url='signin')
def contact(request):
    home = False
    message = ''
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            recipients = ['niamienericn@gmail.com']
            send_mail(sujet, message, email, recipients)
            message = 'Félicitation le message a été bien envoyé'
            context = {
                'message':message,
               'home':home,
                'form':form}
    else:
        form = ContactForm()
        context = {
                'message':message,
               'home':home,
                'form':form}
    return render(request,'contact/contact.html',context)
        
