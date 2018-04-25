from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase

from mailinglist.factories import SubscriberFactory
from mailinglist.models import Subscriber, MailingList


class MockSendEmailToSubscriberTask:

    def setUp(self):
        self.send_confirmation_email_patch = patch(
            'mailinglist.tasks.send_confirmation_email_to_subscriber')
        self.send_confirmation_email_mock = self.send_confirmation_email_patch.start()
        super().setUp()

    def tearDown(self):
        self.send_confirmation_email_patch.stop()
        self.send_confirmation_email_mock = None
        super().tearDown()


class SubscriberCreationTestCase(
    MockSendEmailToSubscriberTask,
    TestCase):

    def test_calling_create_queues_confirmation_email_task(self):
        user = get_user_model().objects.create_user(
            username='unit test runner'
        )
        mailing_list = MailingList.objects.create(
            name='unit test',
            owner=user,
        )
        Subscriber.objects.create(
            email='unittest@example.com',
            mailing_list=mailing_list)
        self.assertEqual(self.send_confirmation_email_mock.delay.call_count, 1)


class SubscriberManagerTestCase(TestCase):

    def testConfirmedSubscribersForMailingList(self):
        mailing_list = MailingList.objects.create(
            name='unit test',
            owner=get_user_model().objects.create_user(
                username='unit test')
        )
        confirmed_users = [
            SubscriberFactory(confirmed=True, mailing_list=mailing_list)
            for n in range(3)]
        unconfirmed_users = [
            SubscriberFactory(mailing_list=mailing_list)
            for n in range(3)]
        confirmed_users_qs = Subscriber.objects.confirmed_subscribers_for_mailing_list(
            mailing_list=mailing_list)
        self.assertEqual(len(confirmed_users), confirmed_users_qs.count())
        for user in confirmed_users_qs:
            self.assertIn(user, confirmed_users)
