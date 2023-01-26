from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from .models import Product,Category
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class ProductListView(LoginRequiredMixin,generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product/product_list.html'

    def get_context_data(self,*args,**kwargs):
        context = super(ProductListView,self).get_context_data(*args,**kwargs)
        category = None
        products_qs = Product.objects.all()
        category = self.request.GET.get('category',None)
        if category:
            if category == 'all':
                products_qs = Product.objects.all()
            else:
                products_qs = Product.objects.filter(category__name__icontains=category)
        query = self.request.GET.get('item',None)
        if query:
            products_qs = Product.objects.filter( Q(name__icontains=query) | Q(category__name__icontains=query)  
            | Q(slug__icontains=query) | Q (category__slug__icontains=query))
            print('search result',products_qs)
        product_paginator = Paginator(products_qs,18)
        product_page_number = self.request.GET.get('page',None)
    
        if product_page_number:
            products = product_paginator.page(product_page_number)
        else:
            products = product_paginator.page(1)
            print(products_qs)
        
        categories = Category.objects.all()
        context['products'] = products
        context['categories'] = categories
        return context


class ProductDetailView(generic.DetailView):
    template_name = 'product/product_detail.html'
    context_object_name = 'product'
    model = Product
    slug_url_kwarg = 'slug'
    
    def get_context_data(self,**kwargs):
        context = super(ProductDetailView,self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        product = Product.objects.get(slug=slug)
        relateds = Product.objects.filter(category=product.category)
        context['relateds'] = relateds

        return context

