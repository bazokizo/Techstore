from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
path('shop/', views.product_list, name='product_list'),
path('phones/', views.phonepage, name='phones'),
path('laptops/', views.laptoppage, name='laptops'),
path('tvs/', views.tvpage, name='tvs'),
path('repairs/', views.repair_form, name='repairs'),
path('', views.homepage, name='home'),
path('categories/<slug:category_slug>/', views.product_list,
	name='product_list_by_category'),
path('<int:id>/<slug:slug>/', views.product_detail,
	name='product_detail'),
path('account/created/',views.signUpView,name = 'signup'),
path('account/signin/',views.signInView,name = 'signin'),
path('account/logout/',views.signoutView,name = 'signout'),
path('search/', views.search, name='search'),

]
