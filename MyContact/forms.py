
# from django import forms
# from django.forms import ModelForm

# from MyContact.models import contact


# class contactform2(forms.Form):
#     firstname=forms.CharField(max_length=10)
#     lastname=forms.CharField(max_length=10)
#     email = forms.EmailField()                    
#     message = forms.CharField(widget=forms.Textarea)  


from django import forms
from MyContact.models import contact
class contactForm3(forms.ModelForm):
    class Meta:
        model = contact
        fields = ('firstname', 'lastname', 'email', 'message')     