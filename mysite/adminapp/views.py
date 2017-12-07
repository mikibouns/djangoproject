from django.shortcuts import render
from authapp.models import AuthUsers
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'users'
    users_list = AuthUsers.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
    content={'title': title,
             'objects': users_list}
    return render(request, 'adminapp/users.html', content)

@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    content={}
    return render(request, 'adminapp/admin_page.html', content)

@user_passes_test(lambda u: u.is_superuser)
def user_update(request):
    content={}
    return render(request, 'adminapp/admin_page.html', content)

@user_passes_test(lambda u: u.is_superuser)
def user_delete(request):
    content={}
    return render(request, 'adminapp/admin_page.html', content)