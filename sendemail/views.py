from django.http import HttpResponse
from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import redirect, render
from sendemail.forms import ContactForm

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email_list = []
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            to_email = form.cleaned_data['to_email']
            email_list.append(to_email)

            try:
                send_mail(subject, message, from_email, email_list)
                return redirect('success')  # Moved inside the try block
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

    return render(request, 'test.html', {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
