# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from .models import Profile
# from django.core.mail import send_mail
# from django.conf import settings

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         user = instance
#         profile = Profile.objects.create(
#             user = user,
#             username = user.username,
#             email = user.email,
#             name = user.first_name,
#         )

#         subject = 'Welcome at my page'
#         message = 'Thanks for register'
        
#         send_mail(
#             subject,
#             message,
#             settings.EMAIL_HOST_USER,
#             [profile.email],
#             fail_silently=False
#         )
