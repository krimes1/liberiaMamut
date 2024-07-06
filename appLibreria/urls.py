from django.urls import path 
from .views import home, contacto, registro, CustomLoginView, custom_logout, cart, add_to_cart, remove_from_cart, add_book, lista_libros, update_book, delete_book, admin_menu
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', lista_libros, name='inicio'),
    path('inicio_de_sesion', CustomLoginView.as_view(), name='login'), 
    path('contacto', contacto, name='contacto'),
    path('registro', registro, name='registro'),
    path('logout/', custom_logout, name='logout'),
    path('cart/', cart, name='cart'),
    path('cart/add/<int:libro_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:libro_id>/', remove_from_cart, name='remove_from_cart'),
    path('add-book/', add_book, name='add_book'),
    path('update-book/<int:libro_id>/', update_book, name='update_book'),
    path('delete-book/<int:libro_id>/', delete_book, name='delete_book'),
    path('admin-menu/', admin_menu, name='admin_menu'),
]
