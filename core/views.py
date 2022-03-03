from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from core.models import Appointment, Reviews


class BaseView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review'] = Reviews.objects.all()
        return context


class AppointmentView(View):
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        message = request.POST.get('message')
        appointment = Appointment()
        appointment.name = name
        appointment.email = email
        appointment.phone = phone
        appointment.date = date
        appointment.message = message
        appointment.save()
        messages.info(request, 'Appointment  received.We will contact you soon!!')
        return redirect('SuccessMessageView')


class ReviewTemplate(TemplateView):
    template_name = 'review_page.html'


class ReviewView(View):
    def post(self, request):
        name = request.POST.get('name')
        tag = request.POST.get('tag')
        image = request.FILES['image']
        patient_status = request.POST.get('patient_status')
        review = request.POST.get('review')
        reviews = Reviews()
        reviews.name = name
        reviews.review_tag = tag
        reviews.image = image
        reviews.status = patient_status
        reviews.review = review
        reviews.save()
        messages.info(request,'Response received..Thankyou!!')
        return redirect('SuccessMessageView')


class NavbarReview(TemplateView):
    template_name = 'navbar.html'


class SuccessMessageView(TemplateView):
    template_name = 'success_message.html'
