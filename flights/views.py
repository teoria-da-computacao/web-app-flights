from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Flight, Passenger
from django.urls import reverse

# Create your views here.
def flights_list_view(request):

    context = {'flights': Flight.objects.all()}
    return render(request, 'flights/list.html',context)


def flight_view(request, flight_id):

    f1 = Flight.objects.get(id=flight_id)
    passengers = f1.passengers.all()

    context = {
        'flight': f1,
        'passengers': passengers,
        'non_passengers': Passenger.objects.exclude(flights=f1.id)
        }

    return render(
        request, 
        'flights/eflight.html', 
        context
        )


def book_view(request, flight_id):
    if request.method == 'POST':

        passenger_id = int(request.POST['passenger_id'])

        passenger = Passenger.objects.get(id=passenger_id)
        flight = Flight.objects.get(id=flight_id)
        print('\n\npassenger: ', passenger)
        print('flight: ', flight)
        passenger.flights.add(flight)

        return HttpResponseRedirect(reverse('flights:flight', args=[flight.id,]))
    
            



