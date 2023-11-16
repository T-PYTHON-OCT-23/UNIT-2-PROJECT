from django.shortcuts import render
from django.http import Http404

cities = [
    {'name': 'Riyadh', 'catchy_phrase': 'The Heart of Saudi Arabia'},
    {'name': 'Abha', 'catchy_phrase': 'A Blissful Retreat'},
    {'name': 'Mekkah', 'catchy_phrase': 'A Spiritual Journey'},
    {'name': 'AlUla', 'catchy_phrase': 'A Timeless Oasis'},
    # Add more cities as needed
]

def get_catchy_phrase(city_name):
    # Function to retrieve the catchy phrase for a given city name
    for city in cities:
        if city['name'].lower() == city_name.lower():
            return city['catchy_phrase']
    return None  # Return None if the city name is not found

def home(request):
    # Home view
    general_description = "Explore the beauty of tourism in Saudi Arabia."
    
    # Send the list of city dictionaries to the template
    context = {'cities': cities, 'general_description': general_description}
    
    return render(request, 'home.html', context)

def city_detail(request, city_name):
    # City detail view
    # Use next to find the city dictionary based on case-insensitive comparison
    city = next((c for c in cities if c['name'].lower() == city_name.lower()), None)
    
    if not city:
        # Return a 404 response if the city is not found
        raise Http404("City not found")
    
    # Prepare the context for the city_detail template
    context = {
        'city': {
            'name': city['name'],
            'numbers': range(1, 5),
            'catchy_phrase': get_catchy_phrase(city_name),
        }
    }
    
    return render(request, 'city_detail.html', context)
