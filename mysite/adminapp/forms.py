from django import forms
from authapp.models import AuthUsers
from authapp.forms import UserEditForm

class UserAdminEditForm(UserEditForm):
    class Meta:
        model = AuthUsers
        fields = '__all__'
