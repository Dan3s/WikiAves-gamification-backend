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

class Achievement(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length= 255, null=False, blank = False)
    description = models.CharField(max_length=255, null=False, blank = False)
    icon = models.ImageField(upload_to='logros/', max_length = 255, null =True, blank = True)
    xp_value = models.IntegerField(null=False, blank = False)

    class Meta:
        verbose_name = 'Logro'
        verbose_name_plural = 'Logros'

    '''USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_name']'''

    def __str__(self):
        return f'{self.name} {self.description}'

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key= True)
    name = models.CharField('Nombres', max_length = 255, null=False, blank = False)
    last_names = models.CharField('Apellidos', max_length = 255, null=False, blank = False)
    username = models.CharField('Nombre de usuario', max_length = 50, unique = True, null=False, blank = False)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True, null=False, blank = False)
    birthdate = models.DateField('Fecha de nacimiento', null=True, blank = True)
    city = models.CharField('Ciudad',max_length = 255, null=False, blank = False)
    region = models.CharField('Región',max_length = 255, null=False, blank = False)
    profile_pic = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank = True)
    xp = models.IntegerField('Experiencia', null=True, blank = True)
    level_name = models.CharField('Nombre de nivel', max_length = 255, default='Colibrí')
    pages_visited = models.IntegerField('Páginas visitadas', null=True, blank = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    achievements = models.ManyToManyField(Achievement, through='UserAchievement')
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_names', 'city', 'region']

    def __str__(self):
        return f'{self.name} {self.last_names}'

class UserAchievement(models.Model):
    id = models.AutoField(primary_key= True)
    unlock_date = models.DateField(null=True, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'LogroUsuario'
        verbose_name_plural = 'LogrosDeUsuario'

    '''USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_name']'''

    def __str__(self):
        return f'{self.id} {self.achievement}'

