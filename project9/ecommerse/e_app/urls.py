from . import views
from django . urls import path
app_name = 'e_app'

urlpatterns = [
    path('', views.allProductsCategory, name='allProductsCategory'),
    path('<slug:c_slug>/', views.allProductsCategory, name='productByCategory'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),
]
