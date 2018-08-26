from django.shortcuts import render, HttpResponse
from activities.models import Activity, Trek, Training, Challenge
import json

def home(request):
    ## UK trips ##
    uk_trips = Activity.objects.all().filter(type="uk trip")

    uk = "<option>Select Destination</option>"

    for trip in uk_trips:
        uk += '<option>' + trip.title + '</option>'

    ## international trips ##
    international_trips = Activity.objects.all().filter(type="international trip")

    international = "<option>Select Destination</option>"

    for trip in international_trips:
        international += '<option>' + trip.title + '</option>'

    ## challenges ##
    challenges = Activity.objects.all().filter(type="challenge")

    challenge = "<option>Select Destination</option>"

    for trip in challenges:
        challenge += '<option>' + trip.title + '</option>'

    ## training ##
    training_events = Activity.objects.all().filter(type="training")

    training = "<option>Select Destination</option>"

    for trip in training_events:
        training += '<option>' + trip.title + '</option>'
    return render(request, 'home.html', {'uk': uk,
                                         'international': international,
                                         'challenge': challenge,
                                         'training': training})

def get_dates(request):
    destination = request.POST.get('dest')

    treks = Trek.objects.all().filter(Title=destination)
    training = Training.objects.all().filter(Title=destination)
    challenge = Challenge.objects.all().filter(Title=destination)

    dates = '<option>Select Date</option>'

    for event in treks:
        dates += '<option>' + event.from_date + '-' + event.to_date + '</option>'
    for event in training:
        dates += '<option>' + event.from_date + '-' + event.to_date + '</option>'
    for event in challenge:
        dates += '<option>' + event.from_date + '-' + event.to_date + '</option>'

    return HttpResponse(json.dumps({'dates': dates}), content_type='application/json')