from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords


class UserManager(BaseUserManager):
    def _create_user(self, names, last_names, username, email, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            names = names,
            last_names = last_names,
            username = username,
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, name, last_names, username, email, password=None, **extra_fields):
        return self._create_user(name, last_names, username, email, password, False, False, **extra_fields)

    def create_superuser(self, name, last_names, username, email, password=None, **extra_fields):
        return self._create_user(name, last_names, username, email, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField('Nombres', max_length = 255)
    last_names = models.CharField('Apellidos', max_length = 255)
    username = models.CharField('Nombre de usuario', max_length = 50, unique = True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True)
    birthdate = models.DateField('Fecha de nacimiento', null=True, blank = True)
    city = models.CharField('Ciudad',max_length = 255)
    region = models.CharField('Región',max_length = 255)
    profile_pic = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank = True)
    xp = models.IntegerField('Experiencia', null=True, blank = True)
    pages_visited = models.IntegerField('Páginas visitadas', null=True, blank = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_names', 'city', 'region']

    def __str__(self):
        return f'{self.name} {self.last_names}'

class Achievement(models.Model):
    name = models.CharField(max_length= 255)
    description = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    icon = models.ImageField(upload_to='logros/', max_length = 255, null =True, blank = True)
    xp_value = models.IntegerField()
    unlock_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Logro'
        verbose_name_plural = 'Logros'

    '''USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_name']'''

    def __str__(self):
        return f'{self.name} {self.description}'
    
class Contribution(models.Model):
    is_Correct = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
