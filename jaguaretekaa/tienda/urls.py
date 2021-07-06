from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('home/', views.home, name="home"),
    path('resultado/', views.resultado, name="resultado"),
    path('producto/', views.producto, name="producto"),
    path('contact/', views.contact, name="contact"),
    # Access
    path('sign_in/', views.signin, name="sign_in"),
    path('sign_up/', views.signup, name="sign_up"),
    # Products
    path('products/', views.products, name="products"),
    path('product/', views.product, name="product"),
    path('products/add/', views.add_product, name="add_product"),
    path('products/edit/<id>', views.edit_product, name="edit_product"),
    path('products/delete/<id>', views.delete_product, name="delete_product"),
    # Categories
    path('categories/', views.categories, name="categories"),
    path('categories/add/', views.add_category, name="add_category"),
    path('categories/edit/<id>', views.edit_category, name="edit_category"),
    path('categories/delete/<id>', views.delete_category, name='delete_category'),
    # Result of search
    path('search/result/', views.result, name="result"),
    # Cart
    path('cart/', views.cart, name="cart"),
    path('cart/add/<id>', views.cart_prod_add, name="cart_prod_add"),
    path('cart/remove/<id>', views.cart_prod_edit, name="cart_prod_edit"),
    path('cart/void', views.void, name="void")
    
]
