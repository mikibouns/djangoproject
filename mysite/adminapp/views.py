from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator

from authapp.models import AuthUsers
from mainapp.views import wallpaper_collections
from authapp.forms import UserRegisterForm
from adminapp.forms import UserAdminEditForm
from mainapp.views import basket_func


class UsersListView(ListView):
    model = AuthUsers
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(UsersListView, self).dispatch(*args, **kwargs)



# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     title = 'users'
#     users_list = AuthUsers.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#
#     content = {'title': title,
#                'basket': basket_func(request),
#                'objects': users_list,
#                'collections': wallpaper_collections,}
#
#     return render(request, 'adminapp/users.html', content)


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
