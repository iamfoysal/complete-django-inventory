from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import get_template, render_to_string

from .models import Profile, User


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created and instance.email:
        Profile.objects.create(user=instance)
        
        message = render_to_string('user/accountmail.html', {'name': instance.get_username()})
        send_mail(
            'Welcome to join inventory management System',
            message,
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            fail_silently= False,
        )
