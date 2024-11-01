from django.urls import path

from MyContact.views import  controleform3

urlpatterns=[
    # path('form2/', controleform2, name='controleform2'),
    path('form3/', controleform3, name='controleform3'),
]
