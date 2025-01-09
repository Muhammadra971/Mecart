from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    Feature_product = Product.objects.order_by('priority')[:4]
    Leatest_product = Product.objects.order_by('-id')[:4]
    context = {
        'Feature_product' : Feature_product,
        'Leatest_product' : Leatest_product
    }
    return render(request,'Home.html',context)
def product(request):
    page = 1
    if request.GET:
        page = request.GET.get('page',1)
    product_list = Product.objects.order_by('-priority')
    Product_pagenater = Paginator(product_list,3)
    product_list = Product_pagenater.get_page(page)
    context = {"product": product_list}
    return render(request,'Products.html',context)
def discription(request,pk):
    product = Product.objects.get(pk=pk)
    data = {'product':product}
    return render(request,'discription.html',data)