from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
class AdminModify(UserAdmin):
    list_display = ['email', 'first_name', 'last_name','dob','country','gender']
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'dob', 'bio', 'gender', 'country', 'profile_pic')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_artist','is_superuser','is_deleted')
        }),
        ('Important dates', {
            'fields': ('date_joined', 'last_login')
        }),
    )

admin.site.register(NewUser,AdminModify)

