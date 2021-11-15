from django import forms
from django.forms import inlineformset_factory
from gwamok.models import Gwamok, Sugang


InlineFormSet = inlineformset_factory(Gwamok,Sugang, fields=['semester', 'title', 'professor', 'day', 'time', 'place', 'avalnum'], extra=2)

class sugangForm(forms.ModelForm):
    class Meta:
        model = Sugang
        fields = '__all__'
        widget_tweaks={
            'GWAMOK' : Gwamok.title,
            'OWNER' : Sugang.owner,

        }