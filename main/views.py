from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView
from .models import Product
from .forms import CreateProductForm

def index(request):
    return render(request, 'main/index.html')


class ViewAbout(TemplateView):
    template_name = 'main/about.html'

class ViewContacts(TemplateView):
    template_name = 'main/contacts.html'

class BBLoginView(LoginView):
    template_name = 'main/login.html'
    success_url = reverse_lazy('products')

class ListProducts(ListView):
    model = Product
    template_name = 'main/products.html'
    context_object_name = 'products'

class CreateProduct(CreateView):
    model = Product
    template_name = 'main/create_product.html'
    success_url = reverse_lazy('products')
    form_class = CreateProductForm

