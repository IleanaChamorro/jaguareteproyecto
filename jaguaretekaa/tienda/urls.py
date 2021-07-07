from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name="tienda"

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    # Access
    path('sign_in/', LoginView.as_view(template_name='login.html'), name="sign_in"),
    path('register/', views.register, name="register"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="logout"),
    # Products
    path('product/<int:id>', views.product, name="product"),
    path('products/add/', views.add_product, name="add_product"),
    path('products/edit/<int:id>', views.edit_product, name="edit_product"),
    path('products/delete/<int:id>', views.delete_product, name="delete_product"),
    # Categories
    path('categories/', views.categories, name="categories"),
    path('categories/add/', views.add_category, name="add_category"),
    path('categories/edit/<int:id>', views.edit_category, name="edit_category"),
    path('categories/delete/<int:id>', views.delete_category, name='delete_category'),
    # Result of search
    path('search/result/', views.result, name="result"),
    # Cart
    path('cart/', views.cart, name="cart"),
    path('cart/add/<int:id>', views.cart_prod_add, name="cart_prod_add"),
    path('cart/remove/<int:id>', views.cart_prod_edit, name="cart_prod_edit"),
    path('cart/void', views.void, name="void")
    
] 
