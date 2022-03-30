from django.shortcuts import render
from django.views import View

from rest_framework import generics, status
from rest_framework.response import Response

from .forms import AddProductForm
from .models import Category, SubCategory, Product
from .serializers import CategorySerializer, SubCategorySerializer, ProductSerializer


class CategoryList(generics.ListAPIView):
    """ API to get all categories """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryList(generics.ListAPIView):
    """ API to get subcategories for a category """
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        queryset = self.queryset.filter(category_id=self.kwargs.get('category_id'))
        return queryset


class CategoryProductList(generics.ListAPIView):
    """ API to get all products for a category """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        sub = SubCategory.objects.filter(category_id=self.kwargs.get('category_id'))
        queryset = self.queryset.filter(sub_category__in=sub)
        return queryset


class SubCategoryProductList(generics.ListAPIView):
    """ API to get all products for a subcategory """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(sub_category_id=self.kwargs.get('subcategory_id'))
        return queryset


class ListDataView(View):
    """ To show all data in table """

    def get(self, request, *args, **kwargs):
        """ Get Method """
        products = Product.objects.filter().order_by('name')
        form = AddProductForm()
        return render(request, 'product_listing.html', {'products': products,
                                                        'form': form, 'title': 'Products'})


class CreateProductView(View):
    """ To show all data in table """

    def post(self, request, *args, **kwargs):
        """ Post Method """
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()

        products = Product.objects.filter().order_by('name')
        form = AddProductForm()
        return render(request, 'product_listing.html', {'products': products,
                                                        'form': form, 'title': 'Products'})
