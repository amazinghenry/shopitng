from django.urls import path
from . import views
from . views import *

app_name = 'shopitapp'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('user/<str:username>', UserProductListView.as_view(), name='user-product'),
    path('allphones/', PhoneListView.as_view(), name='all_phones'),
    path('allcomputers/', ComputerListView.as_view(), name='all_computers'),
    path('alltablets/', TabletListView.as_view(), name='all_tablets'),
    path('alltv/', TvListView.as_view(), name='all_tv'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('product/<int:pk>/update/',
         ProductUpdateView.as_view(), name='product-update'),

    path('product/<int:pk>/delete/',
         ProductDeleteView.as_view(), name='product-delete'),

    path('product/new/', ProductCreateView.as_view(), name='product-create'),
    #     path('search/', SearchResultsList.as_view(), name='search-result'),
    path('search/', views.search_result, name='search_result'),
]
