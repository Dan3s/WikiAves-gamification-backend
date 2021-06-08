from django.contrib import admin

from apps.users.api.serializers.user_serializers import UserProfileStatisticsSerializer
from apps.users.models import User, Achievement, UserAchievement


class UserAdmin(admin.ModelAdmin):#Para modificar como se muestran los registros de la tabla CLiente en el panel de admin.
    list_display=('id', 'username', 'email', 'name', 'last_names', 'is_staff', 'is_superuser')#Esto se hace para mostrar mas campos en el panel de administración
    search_fields=('id', 'username', 'email', 'name', 'last_names', 'is_staff')#Agrega la opción de buscar por estos campos

class AchievementAdmin(admin.ModelAdmin):#Para modificar como se muestran los registros de la tabla CLiente en el panel de admin.
    list_display=('id', 'name', 'description', 'xp_value')#Esto se hace para mostrar mas campos en el panel de administración
    search_fields=('id', 'name', 'description', 'xp_value')#Agrega la opción de buscar por estos campos

class UserAchievementAdmin(admin.ModelAdmin):
    list_display=('id', 'unlock_date', 'user', 'achievement')#Esto se hace para mostrar mas campos en el panel de administración
    search_fields=('id', 'unlock_date', 'user', 'achievement')



# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(UserAchievement, UserAchievementAdmin)
