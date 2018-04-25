from unittest.mock import patch

import factory

from mailinglist.models import Subscriber


class SubscriberFactory(factory.DjangoModelFactory):
    email = factory.Sequence(lambda n: 'foo.%d@example.com' % n)

    class Meta:
        model = Subscriber

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        with patch('mailinglist.models.tasks.'
                   'send_confirmation_email_to_subscriber'):
            return super()._create(model_class=model_class, *args, **kwargs)

