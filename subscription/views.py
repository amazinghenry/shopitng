from subscription.models import Subscribers
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.


def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        send_mail('New subcription email from Shopit',
                  email,
                  settings.EMAIL_HOST_USER,
                  ['henryadodo@zohomail.com'],
                  fail_silently=False)
        Subscribers.objects.create(subscribers_email=email)
        messages.info(request, 'You have been Subscribed!')
        return redirect('/')
    else:
        messages.info(request, 'Unsuccessful')
        return redirect('/')


# def contactagent(request):
#     if request.method == 'POST':
#         message = request.POST['message']
#         send_mail('New Message from:',
#                   message,
#                   '',
#                   ['{}'],
#                   fail_silently=False,
#                   )
