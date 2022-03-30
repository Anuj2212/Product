from django.urls import path
from .views import (
    CategoryList,
    SubCategoryList,
    SubCategoryProductList,
    CategoryProductList,
    ListDataView,
    CreateProductView
)

urlpatterns = [
    path('categorylist/', CategoryList.as_view()),
    path('subcategorylist/<int:category_id>/', SubCategoryList.as_view()),
    path('category/productlist/<int:category_id>/', CategoryProductList.as_view()),
    path('subcategory/productlist/<int:subcategory_id>/', SubCategoryProductList.as_view()),
    path('productlist/', ListDataView.as_view()),
    path('productlist/createproduct/', CreateProductView.as_view(), name='createproduct')
]
