from django.urls import path
from productapp import views

urlpatterns = [
    path("product_list",views.product_list),
    path("product_detail/<int:id>",views.product_detail,name='product_detail'),

]