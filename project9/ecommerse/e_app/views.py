from django.shortcuts import render, get_object_or_404
from . models import category, products
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def allProductsCategory(request, c_slug=None):
    c_page = None
    product_list = None
    if c_slug != None:
        c_page = get_object_or_404(category, slug=c_slug)
        product_list = products.objects.all().filter(var=c_page, available=True)
    else:
        product_list = products.objects.all().filter(available=True)
    paginator = Paginator(product_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except():
        page = 1
    try:
        product = paginator.page(page)
    except(EmptyPage, InvalidPage):
        product = paginator.page(paginator.num_pages)
    return render(request, 'category.html', {'Category': c_page, 'product': product})


def proDetail(request, c_slug, product_slug):
    try:
        product = products.objects.get(var__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'var1': product})
