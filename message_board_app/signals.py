from django.core.mail import mail_managers, EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from message_board import settings
from message_board_app.models import Response


@receiver(post_save, sender=Response)
def notify_message_author(sender, instance, **kwargs):
    template = 'mail/new_response.html'
    email_subject = f'Новый отклик на объявление'
    message_author_email = [instance.message.messageAuthor.email]
    html = render_to_string(
        template_name=template,
        context={
            'response_author': instance.responseAuthor,
            'message': instance.message,
        }
    )

    msg = EmailMultiAlternatives(
        subject=email_subject,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=message_author_email
    )

    msg.attach_alternative(html, 'text/html')
    msg.send()
