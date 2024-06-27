from django.db import models
from django.contrib.auth import get_user_model

from users.models import User



class ServiceRequest(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, default=None, verbose_name='Автор')
    title = models.CharField(max_length=255, verbose_name='Тема заявки', )
    description = models.TextField(blank=True, null=True, verbose_name='Краткое описание')
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Заявка {self.id} от {self.user} {self.created_at}"
    
    class Meta:
        verbose_name='Заявка'
        verbose_name_plural = 'Заявки'