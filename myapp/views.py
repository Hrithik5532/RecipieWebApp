from django.shortcuts import HttpResponse, HttpResponseRedirect, render,redirect
from .forms import *
from django.contrib import messages
from django.db.models import Q  # New

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from .models import *

# Create your views here.

def signup_view(request):
    form = SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'registration/login.html')
    return render(request,'registration/signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
  
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('home')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form':form, 'title':'log in'})

class RecipeListView(ListView):
  model = Recipe
  template_name = 'home.html'
  context_object_name = 'recipes'
  ordering = ['-created_at']


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe-detail.html'
    context_object_name = 'recipes'   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] =  Recipe.objects.get(id = self.kwargs['pk']).author 

        return context

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy('home')
    template_name = 'recipe_confirm_delete.html'

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

class RecipeCreateView(LoginRequiredMixin, CreateView):
  # form_class = recipeform
  fields = ['description','steps','ingre','title','img']
  model = Recipe

  template_name = 'recipe_form.html'
  def test_func(self):
    recipe = self.get_object()
    return self.request.user == recipe.author

  def form_valid(self, form):
    form.instance.author = self.request.user

    return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Recipe
  fields = ['description','steps','ingre','title','img']


  template_name = 'recipe_form.html'



  def test_func(self):
    recipe = self.get_object()
    return self.request.user == recipe.author

  def form_valid(self, form):
    
    form.instance.author = self.request.user

    return super().form_valid(form)
  

def searchBar(request):
  query=request.GET.get('search')
  if query == '':
    return HttpResponseRedirect(reverse('home'))
  
  elif Recipe.objects.filter(Q(description__icontains=query)):
      recipes=Recipe.objects.filter(Q(description__icontains=query))
      
  elif Recipe.objects.filter(Q(title__icontains=query)):
      recipes =Recipe.objects.filter(Q(title__icontains=query))

  elif Recipe.objects.filter(Q(steps__icontains=query)):
      recipes=Recipe.objects.filter(Q(steps__icontains=query))

  elif Recipe.objects.filter(Q(ingre__icontains=query)):
        recipes=Recipe.objects.filter(Q(ingre__icontains=query))

  else:
        messages.warning(request,f'{query} Not Found')
        return HttpResponseRedirect(reverse('home'))
  return render(request,'home.html',{'recipes':recipes})



def test(request):
    if request.method == 'POST':  
      return HttpResponse(request.FILES.get('receipt_field'))