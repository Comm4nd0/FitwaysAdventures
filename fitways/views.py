from django.shortcuts import render, HttpResponse
from activities.models import Activity
from team.models import TeamMember
import json

def home(request):
    ## UK trips ##
    uk_trips = Activity.objects.all().filter(type="uk trip")
    top_uk = Activity.objects.all().filter(type="uk trip").order_by('-date')

    uk = "<option>Select Destination</option>"

    for trip in uk_trips:
        uk += '<option>' + trip.title + '</option>'

    ## international trips ##
    international_trips = Activity.objects.all().filter(type="international trip")
    top_int = Activity.objects.all().filter(type="international trip").order_by('-date')
    international = "<option>Select Destination</option>"

    for trip in international_trips:
        international += '<option>' + trip.title + '</option>'

    ## challenges ##
    challenges = Activity.objects.all().filter(type="challenge")
    top_challenge = Activity.objects.all().filter(type="challenge").order_by('-date')
    challenge = "<option>Select Destination</option>"

    for trip in challenges:
        challenge += '<option>' + trip.title + '</option>'

    ## training ##
    training_events = Activity.objects.all().filter(type="training")
    top_training = Activity.objects.all().filter(type="training").order_by('-date')
    training = "<option>Select Destination</option>"

    for trip in training_events:
        training += '<option>' + trip.title + '</option>'

    team = TeamMember.objects.all()

    return render(request, 'home.html', {'uk': uk,
                                         'uk_trips': uk_trips,
                                         'top_uk': top_uk,
                                         'international': international,
                                         'international_trips': international_trips,
                                         'top_int': top_int,
                                         'challenge': challenge,
                                         'challenges': challenges,
                                         'top_challenge': top_challenge,
                                         'training': training,
                                         'training_events': training_events,
                                         'top_training': top_training,
                                         'team': team,
                                         })

def get_dates(request):
    destination = request.POST.get('dest')

    activity = Activity.objects.all().filter(Title=destination)

    dates = '<option>Select Date</option>'

    for event in activity:
        dates += '<option>' + event.from_date + '-' + event.to_date + '</option>'

    return HttpResponse(json.dumps({'dates': dates}), content_type='application/json')