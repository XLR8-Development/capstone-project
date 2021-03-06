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
import urllib
# If you are using Python 3+, import urllib instead of urllib2
import json
from decimal import Decimal
import requests
import operator

@view_function
def process_request(request):
    utc_time = datetime.utcnow()

    # form = InputForm(request)

    tweet = request.session['tweet']
    isReshare = request.session['isReshare']
    hour = request.session['hour']
    DaysList = request.session['DaysList']
    DayDict = request.session['DayDict']
    maxDict = request.session['maxDict']
    currentMax = request.session['currentMax']
    MonDict = request.session['MonDict']
    TuesDict = request.session['TuesDict']
    WedDict = request.session['WedDict']
    ThursDict = request.session['ThursDict']
    FriDict = request.session['FriDict']
    SatDict = request.session['SatDict']
    SunDict = request.session['SunDict']

    if len(DayDict) < 7:
        # tweet = formData['tweet']
        # isReshare = 0
        # hour = 0
        # MonDict = {}
        # TuesDict = {}
        # WedDict = {}
        # ThursDict = {}
        # FriDict = {}
        # SatDict = {}
        # SunDict = {}
        # DaysList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        # DayDict = {}
        # maxDict = {'Day': 'Monday', 'Hour': 0, 'RetweetCount': 0}
        # currentMax = 0



        # create all the variables and make all the api calls!
        day = DaysList[len(DayDict)]

        hour = 0
        # make call for each hour
        while hour <= 23:

            data =  {

                "Inputs": {

                        "input1":
                        {
                            "ColumnNames": ["Weekday", "Hour", "IsReshare", "RetweetCount", "Country", "text"],
                            "Values": [ [ day, hour, isReshare, "0", "United States", tweet ] ]
                        },        },
                    "GlobalParameters": {
                }
            }

            body = str.encode(json.dumps(data))

            url = 'https://ussouthcentral.services.azureml.net/workspaces/e77673311cc245378b2b51f3f40b5376/services/5be6e9a1fd1c41d083b3971868b14636/execute?api-version=2.0&details=true'
            api_key = '6kRTG9BtU9QYRlqzFj0OhdyZ6+bXeJyKXdbV8lV0jGwon6IwCcM/BhHwEySG5h1WwsWAVY7EmJDg74d14nY3aA==' # Replace this with the API key for the web service
            headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

            req = urllib.request.Request(url, body, headers)

            try:
                response = urllib.request.urlopen(req)

                # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
                # req = urllib.request.Request(url, body, headers)
                # response = urllib.request.urlopen(req)

                result = response.read()
                resultDict = json.loads(result)

                retweetCount = str(resultDict['Results']['output1']['value']['Values'][0][0])
                count = round(float(retweetCount))
                retweetCountRounded = count

                print(retweetCount)

            except urllib.request.HTTPError as error:
                print("The request failed with status code: " + str(error.code))

                # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
                print(error.info())

                print(json.loads(error.read()))


            # store to  appropriate dictionary
            if day == "Monday":
                MonDict[hour] = retweetCountRounded
                print('###### HOUR DICTIONARY: ' + str(MonDict))
                if retweetCountRounded > currentMax:
                    currentMax = retweetCountRounded
                    maxDict['Day'] = "Monday"
                    maxDict['Hour'] = hour
                    maxDict['RetweetCount'] = currentMax
            elif day == "Tuesday":
                TuesDict[hour] = retweetCountRounded
                print('###### HOUR DICTIONARY: ' + str(TuesDict))
                if retweetCountRounded > currentMax:
                    currentMax = retweetCountRounded
                    maxDict['Day'] = "Tuesday"
                    maxDict['Hour'] = hour
                    maxDict['RetweetCount'] = currentMax
            elif day == "Wednesday":
                WedDict[hour] = retweetCountRounded
                print('###### HOUR DICTIONARY: ' + str(WedDict))
                if retweetCountRounded > currentMax:
                    currentMax = retweetCountRounded
                    maxDict['Day'] = "Wednesday"
                    maxDict['Hour'] = hour
                    maxDict['RetweetCount'] = currentMax
            elif day == "Thursday":
                ThursDict[hour] = retweetCountRounded
                print('###### HOUR DICTIONARY: ' + str(ThursDict))
                if retweetCountRounded > currentMax:
                    currentMax = retweetCountRounded
                    maxDict['Day'] = "Thursday"
                    maxDict['Hour'] = hour
                    maxDict['RetweetCount'] = currentMax
            elif day == "Friday":
                FriDict[hour] = retweetCountRounded
                print('###### HOUR DICTIONARY: ' + str(FriDict))
                if retweetCountRounded > currentMax:
                    currentMax = retweetCountRounded
                    maxDict['Day'] = "Friday"
                    maxDict['Hour'] = hour
                    maxDict['RetweetCount'] = currentMax
            elif day == "Saturday":
                SatDict[hour] = retweetCountRounded
                print('###### HOUR DICTIONARY: ' + str(SatDict))
                if retweetCountRounded > currentMax:
                    currentMax = retweetCountRounded
                    maxDict['Day'] = "Saturday"
                    maxDict['Hour'] = hour
                    maxDict['RetweetCount'] = currentMax
            elif day == "Sunday":
                SunDict[hour] = retweetCountRounded
                print('###### HOUR DICTIONARY: ' + str(SunDict))
                if retweetCountRounded > currentMax:
                    currentMax = retweetCountRounded
                    maxDict['Day'] = "Sunday"
                    maxDict['Hour'] = hour
                    maxDict['RetweetCount'] = currentMax

            # hourDict[hour] = retweetCountRounded

            # increment hour
            hour += 1

            # store day of week and dictionary
            if day == "Monday":
                DayDict[day] = MonDict
            elif day == "Tuesday":
                DayDict[day] = TuesDict
            elif day == "Wednesday":
                DayDict[day] = WedDict
            elif day == "Thursday":
                DayDict[day] = ThursDict
            elif day == "Friday":
                DayDict[day] = FriDict
            elif day == "Saturday":
                DayDict[day] = SatDict
            elif day == "Sunday":
                DayDict[day] = SunDict

            print('###### DAY DICTIONARY: '+ str(DayDict))

        # determine highest retweet count
        print(str(maxDict))

        # time schtuff
        TimeResultArray = []

        for i in range(0,24):
            tempResult = TimeResult(str(i) + ":00", random.randrange(100), random.randrange(100), random.randrange(100), random.randrange(100), random.randrange(100), random.randrange(100), random.randrange(100))
            TimeResultArray.append(tempResult)

        # context = {
        #     'tweet':tweet,
        #     'resultDict': resultDict,
        #     'daysList' :DaysList,
        #     'retweetCountRounded' : retweetCountRounded,
        #     'full_results' : DayDict,
        #     'primetime' : maxDict,
        #     'monday' : MonDict,
        #     'tuesday' :TuesDict,
        #     'wednesday' : WedDict,
        #     'thursday' : ThursDict,
        #     'friday' : FriDict,
        #     'saturday' : SatDict,
        #     'sunday' :SunDict,
        # }

        # request.session['tweet'] = tweet
        # request.session['resultDict'] = resultDict
        # request.session['daysList'] = daysList
        # request.session['retweetCountRounded'] = retweetCountRounded
        # request.session['full_results'] = full_results
        # request.session['primetime'] = primetime
        # request.session['DayDict'] = DayDict

        request.session['tweet'] = tweet
        request.session['isReshare'] = isReshare
        request.session['hour'] = hour
        request.session['DaysList'] = DaysList
        request.session['DayDict'] = DayDict
        request.session['maxDict'] = maxDict
        request.session['currentMax'] = currentMax
        request.session['MonDict'] = MonDict
        request.session['TuesDict'] = TuesDict
        request.session['WedDict'] = WedDict
        request.session['ThursDict'] = ThursDict
        request.session['FriDict'] = FriDict
        request.session['SatDict'] = SatDict
        request.session['SunDict'] = SunDict


        return HttpResponseRedirect('/homepage/loading/')

    context = {
        'tweet':tweet,
        'daysList' :DaysList,
        'full_results' : DayDict,
        'primetime' : maxDict,
        'monday' : MonDict,
        'tuesday' :TuesDict,
        'wednesday' : WedDict,
        'thursday' : ThursDict,
        'friday' : FriDict,
        'saturday' : SatDict,
        'sunday' :SunDict,
    }

    return request.dmp_render('/results.html', context)


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
    SUBJECT_CHOICES = [
        [ 'Original', 'This is an original Tweet'],
        [ 'Reshare', "This is a reshare"],
    ]

    def init(self):
        self.fields['subject'] = forms.ChoiceField(label='Tweet Type', choices=InputForm.SUBJECT_CHOICES)
        self.fields['tweet'] = forms.CharField(label='Enter Tweet', max_length=140)
        # self.fields['phone'] = forms.CharField(label="Phone", required=False, max_length=100)
        # self.fields['email'] = forms.EmailField(label='Email (required)', required=True, max_length=100)

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
        subject = self.cleaned_data.get('subject')
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
