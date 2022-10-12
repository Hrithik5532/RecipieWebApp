from django.urls import path
from .views import *


urlpatterns=[
    path('signup',signup_view, name='signup_view')
    ,path('login/',login_view,name='login_view'),
    path('',RecipeListView.as_view(),name='home'),
        path('recipe/<int:pk>', RecipeDetailView.as_view(), name="recipes-detail"),
        path('recipe/create', RecipeCreateView.as_view(), name="recipes-create"),
    path('recipe/<int:pk>/update', RecipeUpdateView.as_view(), name="recipes-update"),
    path('recipe/<int:pk>/delete', RecipeDeleteView.as_view(), name="recipes-delete"),
    path(r'search/',searchBar,name='search'),
    path('test',test,name='test')


]