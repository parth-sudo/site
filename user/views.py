from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm,PaytmForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Paytm
from django.http import HttpResponse
from Paytm import checksum

MERCHANT_KEY = 'xxxxxxxxxxxxxxxx'

def home(request):
    return render(request, 'user/home.html', {})

def register(request):
    form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}")
            form.save()
            return redirect('login')

        else:
            form = UserRegistrationForm()
    return render(request, 'user/register.html',{'form':form})



@login_required
def participate(request):
    form = PaytmForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email  = form.cleaned_data.get('email')
            amount = form.cleaned_data.get('email')
            messages.success(request, f" transaction done for {username}")

            form.save()

            param_dict = {
                'MID': 'DAWJqH26240907898793',
                'ORDER_ID': 'dddgfgfeeed',
                'TXN_AMOUNT': str(amount),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',

                'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest',
            }
           ## param_dict['CHECKSUM_HASH'] = checksum.generate_checksum(param_dict, MERCHANT_KEY)
            return render(request, 'user/paytm.html', {'param_dict': param_dict})

        else:
            form = PaytmForm()

     #request paytm to transfer the amount to your account after payment from user.

    return render(request, 'user/participate.html', {'form':form})

@csrf_exempt
def handlerequest(request):
    #here, PayTM will send you a post request.
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i]=form[i]
        if i =='CHECKSUM_HASH':
            checksum = form[i]

    verify = checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print("Order successful.")
        else:
            print('order was not successful because ' + response_dict['RESPMSG'])
    return render(request, 'user/paymentstatus.html', {'response':response_dict})

def contact(request):
    return render(request, 'user/contact.html')
