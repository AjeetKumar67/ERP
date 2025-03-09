from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, UserRole, Role

@receiver(post_save, sender=CustomUser)
def assign_default_role(sender, instance, created, **kwargs):
    if created:
        default_role = Role.objects.get(name='User')
        UserRole.objects.create(user=instance, role=default_role)
