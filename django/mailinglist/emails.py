import logging
from datetime import datetime
from smtplib import SMTPServerDisconnected

from django.conf import settings
from django.core.mail import send_mail
from django.template import engines, Context
from django.urls import reverse

logger = logging.getLogger(__name__)

CONFIRM_SUBSCRIPTION_HTML = 'mailinglist/email/confirmation.html'

CONFIRM_SUBSCRIPTION_TXT = 'mailinglist/email/confirmation.txt'

SUBSCRIBER_MESSAGE_TXT = 'mailinglist/email/subscriber_message.txt'

SUBSCRIBER_MESSAGE_HTML = 'mailinglist/email/subscriber_message.html'


class EmailTemplateContext(Context):

    @staticmethod
    def make_link(path):
        return settings.MAILING_LIST_LINK_DOMAIN + path

    def __init__(self, subscriber, dict_=None, **kwargs):
        if dict_ is None:
            dict_ = {}
        email_ctx = self.common_context(subscriber)
        email_ctx.update(dict_)
        super().__init__(email_ctx, **kwargs)

    def common_context(self, subscriber):
        subscriber_pk_kwargs = {'pk': subscriber.id}
        unsubscribe_path = reverse('mailinglist:unsubscribe',
                                   kwargs=subscriber_pk_kwargs)
        return {
            'subscriber': subscriber,
            'mailing_list': subscriber.mailing_list,
            'unsubscribe_link': self.make_link(unsubscribe_path),
        }


def send_confirmation_email(subscriber):
    logger.info("in send_confirmation_email. About to send email.")
    mailing_list = subscriber.mailing_list
    confirmation_link = EmailTemplateContext.make_link(
        reverse('mailinglist:confirm_subscription',
                kwargs={'pk': subscriber.id}))
    context = EmailTemplateContext(
        subscriber,
        {'confirmation_link': confirmation_link}
    )
    subject = 'Confirming subscription to {}'.format(mailing_list.name)

    dt_engine = engines['django'].engine
    text_body_template = dt_engine.get_template(CONFIRM_SUBSCRIPTION_TXT)
    text_body = text_body_template.render(context=context)
    html_body_template = dt_engine.get_template(CONFIRM_SUBSCRIPTION_HTML)
    html_body = html_body_template.render(context=context)

    try:
        send_mail(
            subject=subject,
            message=text_body,
            from_email=settings.MAILING_LIST_FROM_EMAIL,
            recipient_list=(subscriber.email,),
            html_message=html_body)
    except SMTPServerDisconnected as e:
        logger.error('sendmail raised an SMTPServerDisconnected %r %s' % (e, e))
    except Exception as e:
        logger.error('sendmail raised generic exception %r %s' % (e, e))


def send_subscriber_message(subscriber_message):
    message = subscriber_message.message
    context = EmailTemplateContext(subscriber_message.subscriber, {
        'body': message.body,
    })

    dt_engine = engines['django'].engine
    text_body_template = dt_engine.get_template(SUBSCRIBER_MESSAGE_TXT)
    text_body = text_body_template.render(context=context)
    html_body_template = dt_engine.get_template(SUBSCRIBER_MESSAGE_HTML)
    html_body = html_body_template.render(context=context)

    utcnow = datetime.utcnow()
    subscriber_message.last_attempt = utcnow
    subscriber_message.save()

    success = send_mail(
        subject=message.subject,
        message=text_body,
        from_email=settings.MAILING_LIST_FROM_EMAIL,
        recipient_list=(subscriber_message.subscriber.email,),
        html_message=html_body)

    if success == 1:
        subscriber_message.sent = utcnow
        subscriber_message.save()
