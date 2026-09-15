import random
import uuid
from datetime import datetime
from django.shortcuts import render, redirect, Http404

DEFAULT_PLACES = [
    {
        'id': '1',
        'title': 'Затишна Кав’ярня',
        'description': 'Чудове місце для ранкової кави та читання книг. Затишна атмосфера та найсмачніший флет-вайт у місті.',
        'place_type': 'Ресторан / Кафе',
        'location': 'вул. Хрещатик, 15',
        'rating': 5,
        'created_at': '2026-09-01 10:00'
    },
    {
        'id': '2',
        'title': 'Секретний Оглядний Майдачик',
        'description': 'Неймовірний краєвид на місто під час заходу сонця. Мало хто знає про цю локацію.',
        'place_type': 'Парк / Прогулянка',
        'location': '',  
        'rating': 4,
        'created_at': '2026-09-05 18:30'
    }
]

def get_user_places(request):
    """Отримання місць із сесії користувача."""
    if 'places' not in request.session:
        request.session['places'] = DEFAULT_PLACES
    return request.session['places']

def home(request):
    places = get_user_places(request)
    random_place = None

    if 'pick_random' in request.GET and places:
        weights = [p['rating'] for p in places]
        random_place = random.choices(places, weights=weights, k=1)[0]
        random_place['short_desc'] = ' '.join(random_place['description'].split()[:5])

    return render(request, 'places/home.html', {'random_place': random_place})

def place_list(request):
    places = get_user_places(request)
    for p in places:
        p['short_desc'] = ' '.join(p['description'].split()[:5])
    return render(request, 'places/place_list.html', {'places': places})

def place_detail(request, place_id):
    places = get_user_places(request)
    place = next((p for p in places if str(p['id']) == str(place_id)), None)
    if not place:
        raise Http404("Місце не знайдено")
    return render(request, 'places/place_detail.html', {'place': place})

def add_place(request):
    from .forms import PlaceForm
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_validate() if hasattr(form, 'is_validate') else form.is_valid():
            places = get_user_places(request)
            new_place = {
                'id': str(uuid.uuid4()),
                'title': form.cleaned_data['title'],
                'description': form.cleaned_data['description'],
                'place_type': form.cleaned_data['place_type'],
                'location': form.cleaned_data['location'],
                'rating': int(form.cleaned_data['rating']),
                'created_at': datetime.now().strftime('%Y-%m-%d %H:%M')
            }
            places.append(new_place)
            request.session['places'] = places
            request.session.modified = True
            return redirect('place_list')
    else:
        form = PlaceForm()

    return render(request, 'places/add_place.html', {'form': form})