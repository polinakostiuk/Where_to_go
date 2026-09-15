from django import forms

TYPE_CHOICES = [
    ('Ресторан', 'Ресторан'),
    ('Кафе', 'Кафе'),
    ('Бар', 'Бар'),
    ('Атракціони', 'Атракціони'),
    ('Культура', 'Культура'),
    ('Інше', 'Інше'),
]

class PlaceForm(forms.Form):
    title = forms.CharField(
       label="Назва місця", 
        max_length=100, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наприклад: Кав’ярня біля дому'}) 
    )
    description = forms.CharField(
        label="Опис місця✍🏻", 
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Наприклад: Дуже затишна атмосфера', 'rows': 4}) 
    )
    place_type = forms.ChoiceField(
        label="Тип місця🌄", 
        choices=TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    location = forms.CharField(
        label="Локація / Адреса📍", 
        max_length=150, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Залиште порожнім для Secret place👀'})
    )
    rating = forms.IntegerField(
        label="Особистий рейтинг (1-5)🤩", 
        min_value=1, 
        max_value=5,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5})
    )