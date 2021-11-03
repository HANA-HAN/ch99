from django.shortcuts import render
from django.views.generic import ListView, DetailView
from photo.models import Album,Photo
from django.views.generic import FormView
from photo.form import PhotoSearchForm
from django.db.models import Q
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import  reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from mysite.views import OwnerOnlyMixin
from photo.form import PhotoInlineFormSet
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


class PhotoCV(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ('album', 'title', 'image','description')
    success_url = reverse_lazy('photo:index')

    def form_valid(self, form):
        form.instance.owner=self.request.user
        return super().form_valid(form)

class PhotoChangeLV(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'photo/photo_change_list.html'

    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)

class PhotoUV(OwnerOnlyMixin, UpdateView):
    model = Photo
    fields = ('album','title','image','description')
    success_url = reverse_lazy('photo:index')

class PhotoDelV(OwnerOnlyMixin, DeleteView):
    model = Photo
    success_url = reverse_lazy('photo:index')

class AlbumChangeLV(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'photo/album_change_list.html'

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)

class AlbumDelV(OwnerOnlyMixin, DeleteView):
    model = Album
    success_url = reverse_lazy('photo:index')

class AlbumPhotoCV(LoginRequiredMixin, CreateView):
    model = Album
    fields = ('name', 'description')
    success_url = reverse_lazy('photo:index')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset']=PhotoInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset']=PhotoInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.ownr=self.request.user
        context=self.get_context_data()
        formset=context['formset']
        for photoform in formset:
            photoform.instance.owner=self.request.user
        if formset.is_vaild():
            self.object=form.save()
            formset.instance=self.object
            formset.save()

            return redirect(self.get_success_url())

        else:
            return self.render_to_response(self.get_context_data(form=form))