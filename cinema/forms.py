from django import forms
from .models import Post, Movies, Cinema

CATEGORIES = (  
    ('LAB', 'labor'),
    ('CAR', 'cars'),
    ('TRU', 'trucks'),
    ('WRI', 'writing'),
)
LOCATIONS = (  
    ('BRO', 'Bronx'),
    ('BRK', 'Brooklyn'),
    ('QNS', 'Queens'),
    ('MAN', 'Manhattan'),
)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text',)


class MoviesForm(forms.ModelForm):  
    error_css_class = 'error'

    movie = forms.ModelChoiceField(queryset = Movies.objects.all().order_by('name') )
    cinema = forms.ModelChoiceField(queryset= Cinema.objects.all().order_by('name'), required=True )

    class Meta:
        model = Movies
        fields = ('movie','cinema',)
