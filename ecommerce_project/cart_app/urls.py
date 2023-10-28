from django.urls import path

from . import views
app_name='cart_app'
urlpatterns = [
     path('add/<int:product_id>/',views.add_cart,name='add'),
     path('', views.cart_detail ,name='cart_detail'),
     path('remove/<int:product_id>',views.cart_remove,name='remove'),
     path('remove/<int:product_id>',views.fullremove,name='fullremove')
    ]


