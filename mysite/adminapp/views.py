from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator

from authapp.models import AuthUsers
from mainapp.models import Collections, CollectionsImg
from mainapp.views import wallpaper_collections
from authapp.forms import UserRegisterForm
from adminapp.forms import ProductEditForm, CollectionsEditForm, UserAdminEditForm
from mainapp.views import basket_func


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'users'
    users_list = AuthUsers.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    content = {'title': title,
               'basket': basket_func(request),
               'objects': users_list,
               'collections': wallpaper_collections,}

    return render(request, 'adminapp/users.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'create_user'
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = UserRegisterForm()

    content = {'title': title,
               'basket': basket_func(request),
               'collections': wallpaper_collections,
               'update_form': user_form}

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'user_update'
    edit_user = get_object_or_404(AuthUsers, pk=pk)
    if request.method == 'POST':
        edit_form = UserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:user_update', args=[edit_user.pk]))
    else:
        edit_form = UserAdminEditForm(instance=edit_user)

    content = {'title': title,
               'basket': basket_func(request),
               'update_form': edit_form,
               'collections': wallpaper_collections,}

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'user_delete'
    user = get_object_or_404(AuthUsers, pk=pk)
    if request.method == 'POST':
        # user.delete()
        user.is_active = False
        user.save()

    content = {'title': title,
               'basket': basket_func(request),
               'user_to_delete': user}

    return render(request, 'adminapp/user_delete.html', content)

####################################################################################################

class ProductListView(ListView):
    model = CollectionsImg
    # paginate_by = 2
    template_name = 'adminapp/products_list.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(ProductListView, self).dispatch(*args, **kwargs)

# @user_passes_test(lambda u: u.is_superuser)
# def products(request):
#     title = 'products_list'
#     context = {'title': title}
#     return render(request, 'adminapp/products_list.html', context)

@user_passes_test(lambda u: u.is_superuser)
def products_create(request):
    title = 'products_crete'
    context = {'title': title}
    return render(request, 'adminapp/products_list.html', context)

@user_passes_test(lambda u: u.is_superuser)
def products_update(request, pk):
    title = 'products_update'
    edit_product = get_object_or_404(CollectionsImg, pk=pk)
    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:products_update', args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)

    content = {'title': title,
               'update_form': edit_form,
               'collections': wallpaper_collections,}

    return render(request, 'adminapp/products_update.html', content)

@user_passes_test(lambda u: u.is_superuser)
def products_delete(request, pk):
    title = 'products_delete'
    product = get_object_or_404(CollectionsImg, pk=pk)
    if request.method == 'POST':
        # user.delete()
        product.img_is_active = False
        product.save()

    context = {'title': title,
               'product_to_delete': product,
               'collections': wallpaper_collections}

    return render(request, 'adminapp/products_delete.html', context)

####################################################################################################

class CollectionsListView(ListView):
    model = Collections
    # paginate_by = 2
    template_name = 'adminapp/collections_list.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(CollectionsListView, self).dispatch(*args, **kwargs)

# @user_passes_test(lambda u: u.is_superuser)
# def products(request):
#     title = 'products_list'
#     context = {'title': title}
#     return render(request, 'adminapp/products_list.html', context)

@user_passes_test(lambda u: u.is_superuser)
def collections_create(request):
    title = 'collections_crete'
    context = {'title': title}
    return render(request, 'adminapp/products_list.html', context)

@user_passes_test(lambda u: u.is_superuser)
def collections_update(request, pk):
    title = 'collections_update'
    edit_collections = get_object_or_404(Collections, pk=pk)
    if request.method == 'POST':
        edit_form = CollectionsEditForm(request.POST, request.FILES, instance=edit_collections)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:collections_update', args=[edit_collections.pk]))
    else:
        edit_form = CollectionsEditForm(instance=edit_collections)

    content = {'title': title,
               'update_form': edit_form,
               'collections': wallpaper_collections,}

    return render(request, 'adminapp/products_update.html', content)

@user_passes_test(lambda u: u.is_superuser)
def collections_delete(request, pk):
    title = 'collections_delete'
    context = {'title': title}
    return render(request, 'adminapp/products_delete.html', context)