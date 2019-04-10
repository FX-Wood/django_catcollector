from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})

def cats_show(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/show.html', {'cat': cat})


class CatCreate(CreateView):
    model = Cat
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save(commit=false)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/cats')

class CatUpdate(UpdateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # we are gonna add some stuff here
        self.object.save()
        return HttpResponseRedirect(f"/cats/{str(self.object.pk)}")

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats'
