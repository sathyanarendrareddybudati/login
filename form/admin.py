from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from form.models import User


class UserModelAdmin(BaseUserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'email', 'Name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('Name',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'Name', 'password', 'confirm_password'),
        }),
    )
    search_fields = ('email',)
    ordering = ('id', 'email',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)
