from .models import Collection, CollectionType, SiteUser, CollectionItem, UserComment
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages


def index(request):
    return render(request, 'CollectAll/index.html')


class CollectionListView(generic.ListView):
    model = Collection

    def get_queryset(self):
        return Collection.objects.filter(private=False).filter(parent=None)


class CollectionDetailView(generic.DetailView):
    model = Collection


class PersonalCollectionListView(LoginRequiredMixin, generic.ListView):
    model = Collection
    template_name = 'CollectAll/personal_list.html'

    def get_queryset(self):
        return Collection.objects.filter(siteUser=self.request.user).filter(parent=None)


class ProfileView(generic.DetailView):
    model = SiteUser

    def user_profile(self):
        return self.request.user == SiteUser


class CollectionCreate(LoginRequiredMixin, CreateView):
    model = Collection
    fields = ['name', 'private', 'favorite', 'notes', 'collectionType', 'siteUser']


class CollectionUpdate(LoginRequiredMixin, UpdateView):
    model = Collection
    fields = ['name', 'private', 'favorite', 'notes', 'collectionType']


def collection_delete(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    try:
        collection.delete()
        messages.success(request, (collection.name + " has been deleted"))
    except:
        messages.success(request, (collection.name + " cannot be deleted"))
    return redirect('personal_list')
