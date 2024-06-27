from app.settings import TELEGRAM_BOT_TOKEN, YOUR_PERSONAL_CHAT_ID
from django.db.models.signals import post_save
from django.dispatch import receiver
from catalog.models import ServiceRequest
from .telegram_bot import send_telegram_message
import asyncio
from users.models import User
from django.utils import timezone
import pytz

@receiver(post_save, sender=ServiceRequest)
def send_telegram_notification(sender, instance, created, **kwargs):
    if created:
        user = instance.user 
        phone_number = user.phone_number  
        local_time = instance.created_at.astimezone(pytz.timezone('Europe/Moscow'))
        message = f"""
*Новая заявка на услуги*
*Пользователь:* {instance.user}
*Номер телефона:* {phone_number}
*Тема:* {instance.title}
*Описание:* {instance.description or 'не указан'}
*Дата создания:* {local_time.strftime('%Y-%m-%d %H:%M:%S')}
        """
        asyncio.run(send_telegram_message(TELEGRAM_BOT_TOKEN, YOUR_PERSONAL_CHAT_ID, message))
        
        
        
