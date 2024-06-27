from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


class User(AbstractUser):
    photo = models.ImageField(
        upload_to='users/images/%Y/%m/%d/', 
        blank=True, 
        null=True, 
        verbose_name='Фотография'
        )
    
    phone_number = models.CharField(
        validators=[RegexValidator(regex=r'^\+?7(?:[0-9]{8,15}$)')],
        max_length=17,
        blank=True,
        null=True,
        verbose_name='Номер телефона'
    )
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"