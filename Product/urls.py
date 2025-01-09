
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='home'),
    path('list_products',views.product,name='products'),
    path('item/<pk>',views.discription,name='item')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
