from django.shortcuts import render
from django.http import HttpResponse

from MyContact.forms import contactForm3

# from MyContact.forms import contactform2

# Create your views here.


# def controleform2(request):
#     if request.method == 'POST':  # S'il s'agit d'une requête POST
#         form = contactform2(request.POST)  # Nous reprenons les données
#         if form.is_valid():  # Nous vérifions que les données envoyées sont valides
           
#             # Ici nous pouvons traiter les données du formulaire
#             f = form.cleaned_data['firstname']
#             l = form.cleaned_data['lastname']
#             e = form.cleaned_data['email']
#             m = form.cleaned_data['message']
           
#             # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer
#             contact = contact.objects.create(firstname=f, lastname=l, email=e, message=m)

#             return HttpResponse('<h2>Data has been submitted</h2>')  # Message de succès
#     else:  # Si ce n'est pas du POST, c'est probablement une requête GET
#         form = contactform2()  # Nous créons un formulaire vide
   
#     return render(request, "myform2.html", {'mycontactform2': form})


def controleform3(request):
    if request.method == 'POST':
        form = contactForm3(request.POST)
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the form data to the database
            return HttpResponse('<h2>Data has been submitted</h2>')  # Success message
    else:
        form = contactForm3()  # Create an empty form
    return render(request, "myform3.html", {'mycontactform3': form})  # Render the form
