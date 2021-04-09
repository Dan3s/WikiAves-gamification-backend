from django.contrib import admin
from apps.users.models import User, Achievement


class UserAdmin(admin.ModelAdmin):#Para modificar como se muestran los registros de la tabla CLiente en el panel de admin.
    list_display=('id', 'username', 'email', 'name', 'last_names', 'is_staff', 'is_superuser')#Esto se hace para mostrar mas campos en el panel de administración
    search_fields=('id', 'username', 'email', 'name', 'last_names', 'is_staff')#Agrega la opción de buscar por estos campos

class AchievementAdmin(admin.ModelAdmin):#Para modificar como se muestran los registros de la tabla CLiente en el panel de admin.
    list_display=('id', 'name', 'description', 'active', 'xp_value', 'unlock_date', 'user')#Esto se hace para mostrar mas campos en el panel de administración
    search_fields=('id', 'name', 'description', 'active', 'xp_value', 'unlock_date', 'user')#Agrega la opción de buscar por estos campos




# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Achievement, AchievementAdmin)
