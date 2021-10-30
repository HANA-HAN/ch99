from django.shortcuts import render
from django.views.generic import ListView, DetailView
from photo.models import Album,Photo
from django.views.generic import FormView
from photo.form import PhotoSearchForm
from django.db.models import Q
from django.shortcuts import render
# Create your views here.

class AlbumLV(ListView):
    model = Album

class AlbumDV(DetailView):
    model = Album

class PhotoDV(DetailView):
    model = Photo


class SearchFormView(FormView):
    form_class = PhotoSearchForm
    template_name = 'photo/photo_search.html'

    def form_valid(self, form):
        searchWord=form.cleaned_data['search_word']
        photo_list=Photo.objects.filter(Q(title__icontains=searchWord)|Q(description__icontains=searchWord)).distinct()

        context={}
        context['form']=form
        context['search_word']=searchWord
        context['object_list']=photo_list

        return render(self.request, self.template_name,context)