from django.shortcuts import render, redirect
import datetime
from .models import * 
import os
from .forms import SubscribersForm, MessageForm, UserLoginForm, ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame
from django.http import FileResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
		logout,
		authenticate,
		login,
		get_user_model
		)


def base(request):
	if request.method == "POST":
		form = SubscribersForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Subscription Successful!')
			return redirect('/')
	else:
		form = SubscribersForm()
	context = {'form': form,}
	return render(request, 'base.html', context)

def index(request):
	if request.method == "POST":
		form = SubscribersForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Subscription Successful!')
			return redirect('/')
	else:
		form = SubscribersForm()
    
	return render(request, 'index.html', {'form': form,})

def about(request):
	if request.method == "POST":
		form = SubscribersForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Subscription Successful!')
			return redirect('/')
	else:
		form = SubscribersForm()
    
	return render(request, 'about.html', {'form': form,})

def products(request):
	if request.method == "POST":
		form = SubscribersForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Subscription Successful!')
			return redirect('/')
	else:
		form = SubscribersForm()

	page = "products"
	context = {'page' : page, 'form': form,}
	return render(request, 'products.html', context)

def extra_high_density(request):
	if request.method == "POST":
		form = SubscribersForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Subscription Successful!')
			return redirect('/')
	else:
		form = SubscribersForm()
    
	context = {'form': form,}
	return render(request, 'extra_high_density.html', context)

def high_density(request):
	if request.method == "POST":
		form = SubscribersForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Subscription Successful!')
			return redirect('/')
	else:
		form = SubscribersForm()
    
	context = {'form': form,}
	return render(request, 'high_density.html', context)


def medium_density(request):
	if request.method == "POST":
		form = SubscribersForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Subscription Successful!')
			return redirect('/')
	else:
		form = SubscribersForm()
    
	context = {'form': form,}
	return render(request, 'medium_density.html', context)


def high_quality(request):
	if request.method == "POST":
		form = SubscribersForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Subscription Successful!')
			return redirect('/')
	else:
		form = SubscribersForm()
    
	context = {'form': form,}
	return render(request, 'high_quality.html', context)


def normal_quality(request):
	if request.method == "POST":
		form = SubscribersForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Subscription Successful!')
			return redirect('/')
	else:
		form = SubscribersForm()
    
	context = {'form': form,}
	return render(request, 'normal_quality.html', context)


def furniture(request):
	if request.method == "POST":
		form = SubscribersForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Subscription Successful!')
			return redirect('/')
	else:
		form = SubscribersForm()
    
	context = {'form': form,}
	return render(request, 'furniture.html', context)


def cusions_and_foams(request):
	if request.method == "POST":
		form = SubscribersForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Subscription Successful!')
			return redirect('/')
	else:
		form = SubscribersForm()
    
	context = {'form': form,}
	return render(request, 'cusions_and_foams.html', context)

def contact_us(request):
	if request.method == "POST":
		contact_form = ContactForm(request.POST)
		if contact_form.is_valid():
			contact_form.save()
			name = contact_form.cleaned_data.get('name')
			from_email = contact_form.cleaned_data.get('email', '')
			subject = contact_form.cleaned_data.get('subject')
			message = contact_form.cleaned_data.get('message')
			mail_msg = str(message) + " " + str(from_email)
			send_mail(
				subject,
				mail_msg,
				from_email,
				['jacobdjango7@gmail.com'],
				fail_silently=False,
			)
			messages.success(request, 'Message has been sent Successfully!')
			return redirect('contact_us')
		form = SubscribersForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Subscription Successful!')
			return redirect('/')

	else:
		form = SubscribersForm()
		contact_form = ContactForm()
	context = {'form': form, 'contact_form': contact_form,}
	return render(request, 'contact-us.html', context)


def catalog(request):
    filepath = os.path.join('static', 'assets/pdfs/combinepdf.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')


@login_required
def mail(request):
	emails = Subscriber.objects.all()
	data_frame = read_frame(emails, fieldnames=['email'])
	email_list = data_frame['email'].values.tolist()
	if request.method == "POST":
		form = MessageForm(request.POST)
		if form.is_valid():
			form.save()
			subject = form.cleaned_data.get('subject')
			message = form.cleaned_data.get('body')
			send_mail(
				subject,
				message,
				'',
				email_list,
				fail_silently=False,
			)
			messages.success(request, 'Message has been sent to the mail list Successfully!')
			return redirect('mail')
	else:
		form = MessageForm()
	context = {'form': form,}
	return render(request, 'mail.html', context)

def login_view(request):
	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		if next:
			return redirect('next')
		return redirect('/')
	return render(request, 'login.html', {'form': form})



def logout_view(request):
	logout(request)
	return redirect('/')