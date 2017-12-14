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
    utc_time = datetime.utcnow()

    form = InputForm(request)


    if form.is_valid():
        form.commit()
        messages.success(request, 'Your text was submitted.')
        return HttpResponseRedirect('/homepage/index.recommendations')

    context = {
        # sent to index.html:
        'utc_time': utc_time,
        # sent to index.html and index.js:
        jscontext('utc_epoch'): utc_time.timestamp(),
        'form': form,
    }

    return request.dmp_render('index.html', context)


class TimeResult(object):
    hour = ""
    mon = 0
    tue = 0
    wed = 0
    thu = 0
    fri = 0
    sat = 0
    sun = 0


    # The class "constructor" - It's actually an initializer
    def __init__(self, hour, mon, tue, wed, thu, fri, sat, sun):
        self.hour = hour
        self.mon = mon
        self.tue = tue
        self.wed = wed
        self.thu = thu
        self.fri = fri
        self.sat = sat
        self.sun = sun

@view_function
def recommendations(request):

    TimeResultArray = []

    for i in range(0,24):
        tempResult = TimeResult(str(i) + ":00", random.randrange(100), random.randrange(100), random.randrange(100), random.randrange(100), random.randrange(100), random.randrange(100), random.randrange(100))
        TimeResultArray.append(tempResult)


    context = {
        'result_time' : '4:00PM',
        'result_date' : 'WED, 12/14/2017',
        'full_results' : TimeResultArray,
    }
    return request.dmp_render('index.recommendations.html', context)


class InputForm(FormMixIn, forms.Form):
    form_submit = 'Analyze Tweet'
    # SUBJECT_CHOICES = [
    #     [ 'Inquiry', 'I want to know more about XLR8'],
    #     [ 'Estimate', "I need an estimate for my awesome project"],
    #     [ 'Support', 'I have a technical issue'],
    #     ['Other', 'Other'],
    # ]

    def init(self):
        self.fields['tweet'] = forms.CharField(label='Enter Tweet', max_length=140)
        # self.fields['phone'] = forms.CharField(label="Phone", required=False, max_length=100)
        # self.fields['email'] = forms.EmailField(label='Email (required)', required=True, max_length=100)
        # self.fields['subject'] = forms.ChoiceField(label='Subject', choices=InputForm.SUBJECT_CHOICES)
        # self.fields['message'] = forms.CharField(label='Message (required)', max_length=1000,
        #     widget=forms.Textarea())


    # allows you to modify input such as change it to an int, etc.
    def clean_name(self):
        tweet = self.cleaned_data.get('tweet')
        parts = name.strip().split()
        if len(parts) <= 1:
            raise forms.ValidationError('Please enter tweet')

        return tweet

    def commit(self):
        tweet = self.cleaned_data.get('tweet')
        # from_email = self.cleaned_data.get('email')
        # subject = self.cleaned_data.get('subject')
        # message = self.cleaned_data.get('message')
        # to_email = 'info@xlr8dev.com'
        # #info@xlr8dev.com
        # if from_email != '':
        #     send_mail(
        #             subject,
        #             message,
        #             from_email,
        #             [to_email],
        #             fail_silently=False,
        #         )
