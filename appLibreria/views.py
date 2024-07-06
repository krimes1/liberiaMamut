from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import UserForm, LoginForm
from django.contrib.auth import logout
from .models import libro, CartItem
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import LibroForm
# Create your views here.

def home(request):
    return render(request, 'index.html')

class CustomLoginView(LoginView):
    template_name = 'Login.html'
    form_class = LoginForm

def contacto(request):
    return render(request, 'contacto.html')

def registro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            nick1 = form.cleaned_data['username']
            messages.success(request, f'Usuario {nick1} creado con exito')
            return redirect('inicio')
    else:
        form = UserForm()

    contexto = { 'form' : form }

    return render(request,'signup.html', contexto)

def custom_logout(request):
    logout(request)
    return redirect('inicio')

@login_required
def add_to_cart(request, libro_id):
    libro_item = libro.objects.get(id_libro=libro_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, libro=libro_item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def remove_from_cart(request, libro_id):
    cart_item = CartItem.objects.get(user=request.user, libro_id=libro_id)
    cart_item.delete()
    return redirect('cart')

@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})

def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def add_book(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = LibroForm()
    return render(request, 'add_book.html', {'form': form})

def lista_libros(request):
    libros = libro.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})

@login_required
@user_passes_test(is_admin)
def update_book(request, libro_id):
    libro_item = get_object_or_404(libro, id_libro=libro_id)
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES, instance=libro_item)
        if form.is_valid():
            form.save()
            return redirect('admin_menu')
    else:
        form = LibroForm(instance=libro_item)
    return render(request, 'update_book.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def delete_book(request, libro_id):
    libro_item = get_object_or_404(libro, id_libro=libro_id)
    if request.method == 'POST':
        libro_item.delete()
        return redirect('admin_menu')
    return render(request, 'delete_book.html', {'libro': libro_item})

@login_required
@user_passes_test(is_admin)
def admin_menu(request):
    libros = libro.objects.all()
    return render(request, 'admin_menu.html', {'libros': libros})