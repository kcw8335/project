from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager, BaseUserManager
)
from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email', unique=True)
    username = models.CharField('이름', max_length=30, blank=True)
    registered = models.CharField('거주지', max_length=80, blank=True)
    phone = models.CharField('전화번호', max_length=80, blank=True)
    is_staff = models.BooleanField('스태프 권한', default=False)
    is_active = models.BooleanField('사용중', default=True)
    date_joined = models.DateTimeField('가입일', default=timezone.now)

    objects = UserManager()
    #USERNAME_FIELD = 'name'
    #REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'email'                     # email을 사용자의 식별자로 설정
    REQUIRED_FIELDS = ['username']                   # 필수입력값




"""
    email = models.EmailField('email', unique=True)
    username = models.CharField('이름', max_length=30, blank=True)
    registered = models.CharField('거주지', max_length=80, blank=True)
    phone = models.CharField('전화번호', max_length=80, blank=True)
    is_staff = models.BooleanField('스태프 권한', default=False)
    is_active = models.BooleanField('사용중', default=True)
    date_joined = models.DateTimeField('가입일', default=timezone.now)
"""
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password,  **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        username =self.get_by_natural_key(username)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, adress, phone_number, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        username =self.get_by_natural_key(username)
        user = self.model(email=email, username=username,registered=adress, phone=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

# 생략
