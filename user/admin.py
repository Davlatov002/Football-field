from django.contrib import admin
from .models import CustomUser

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'roles')
    search_fields = ('username','email')
    exclude = ('last_login','superuser_status', 'groups', 'user_permissions','is_active', 'is_staff', 'date_joined', 'is_superuser')
    list_filter = ('roles', )

admin.site.register(CustomUser, UserAdmin)
