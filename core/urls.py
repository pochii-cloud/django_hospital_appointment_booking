from django.urls import path

from core.views import BaseView, AppointmentView, ReviewView, ReviewTemplate, NavbarReview, SuccessMessageView

urlpatterns = [
    path('', BaseView.as_view(), name='BaseView'),
    path('AppointmentView/', AppointmentView.as_view(), name='AppointmentView'),
    path('ReviewTemplate/', ReviewTemplate.as_view(), name='ReviewTemplate'),
    path('ReviewView/', ReviewView.as_view(), name='ReviewView'),
    path('NavbarReview/', NavbarReview.as_view(), name='NavbarReview'),
    path('SuccessMessageView/', SuccessMessageView.as_view(), name='SuccessMessageView'),
]
