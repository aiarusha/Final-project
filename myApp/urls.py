from django.urls import path

from . import views

urlpatterns = [

	path('', views.home, name='home'),
	path('store', views.store, name="store"),
	path('cart/', views.cart, name="cart"),

	path('update_item/', views.updateItem, name="update_item"),

	path('', views.home, name='home'),
	path('home', views.home),
	path('men', views.men),
	path('women', views.women),
	path('aboutus', views.aboutus),
	path('register', views.signUpPage, name='register'),
	path('login', views.signInPage, name='login'),
	path('logout', views.signOutPage, name='signOut'),
	path('contact', views.contact, name='contact'),
	path('skincare', views.skincare, name='skincare'),
	path('sales', views.sales, name='sales'),
	path('new', views.new, name='new'),


]