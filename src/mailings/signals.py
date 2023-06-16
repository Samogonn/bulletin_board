from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from board.models import Response


@receiver(post_save, sender=Response)
def send_new_response_notification(sender, instance, created, **kwargs):
    if created:
        subject = f"Новый отклик на объявление {instance.announcement}"
        recipient_email = instance.announcement.author.email

        send_mail(
            subject,
            instance.text,
            from_email=None,
            recipient_list=(recipient_email,),
            fail_silently=False,
        )


@receiver(pre_save, sender=Response)
def send_on_response_accept(sender, instance, **kwargs):
    if instance.id is None:
        pass
    else:
        previous = Response.objects.get(id=instance.id)
        if previous.is_accepted != instance.is_accepted:
            subject = f"Ваш отклик {instance.text} принят"
            recipient_email = instance.author.email

            send_mail(
                subject,
                instance.text,
                from_email=None,
                recipient_list=(recipient_email,),
                fail_silently=False,
            )
