from django.urls import path

from . import views
app_name='ecommerce_app'
urlpatterns = [

    path('', views.AllProdutCat, name='AllProdutCat'),
    path('<slug:c_slug>/',views.AllProdutCat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodetail, name='productdetail')
   ]