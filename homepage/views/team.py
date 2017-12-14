from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django.conf import settings
from django_mako_plus import view_function
from .. import dmp_render, dmp_render_to_string
from django import forms
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.mail import send_mass_mail
from formlib.form import FormMixIn
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
import random

@view_function
def process_request(request):

    context = {
    
    }

    return request.dmp_render('team.html', context)
