from django.urls import path
from .views import index, about, contact, CategoryView, ItemDetailView


app_name = 'core'


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('business/', about, name='business'),
    path('contact/', contact, name='contact'),
    path('category/', CategoryView.as_view(), name='category'),
    path('product/<slug>/', ItemDetailView.as_view(),
         name='product'),

]
