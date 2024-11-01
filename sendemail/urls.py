from django.urls import path

from sendemail.views import contactView, successView

urlpatterns=[
    path('contact/', contactView, name='contact'),  # URL for the contact form
    path('success/', successView, name='success'),  # URL for success page
    ]
