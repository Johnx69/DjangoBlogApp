from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .form import UserChangeForm, UserCreationForm
from .models import User
from django.utils.translation import gettext_lazy as _

# Register your models here.


class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    form = UserChangeForm
    add_form = UserCreationForm
    model = User

    list_display = [
        "pkid",
        "id",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    ]

    list_display_links = ["pkid", "id", "email"]

    list_filter = ["email", "is_staff", "is_active"]

    fieldsets = (
        (_("Login Credentials"), {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            (
                None,
                {
                    "classes": ("wide",),
                    "fields": (
                        "email",
                        "first_name",
                        "last_name",
                        "password1",
                        "password2",
                    ),
                },
            )
        ),
    )
    search_fields = ["email", "first_name", "last_name"]


admin.site.register(User, UserAdmin)
