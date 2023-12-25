from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('about/', ViewAbout.as_view(), name='about'),
    path('contacts/', ViewContacts.as_view(), name='contacts'),
    path('login/', BBLoginView.as_view(), name='login'),
    path('products/', ListProducts.as_view(), name='products'),
    path('create_product/', CreateProduct.as_view(), name='create_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)