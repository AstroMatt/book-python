import logging
from django.contrib.auth import get_user_model
from django.test import TestCase


User = get_user_model()


logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime).19s] %(levelname).4s %(message)s')


class TestCase(TestCase):
    pass


class TestURL(TestCase):
    SHOW_VALID = False
    SHOW_SKIPPED = False

    assert_http_status = [
    ]

    def setUp(self):
        self.logger = logging.getLogger(__name__)
        self.user = User.objects.create_superuser('testrunner', 'test@test.com', 'testrunner')
        self.client.login(username='testrunner', password='testrunner')

    def tearDown(self):
        self.client.logout()
        self.user.delete()

    def test_url(self):
        errors = []

        for row in self.assert_http_status:
            url = row['url']
            status = row['status']
            skip = row.get('skip', False)

            if skip:
                if self.SHOW_SKIPPED:
                    msg = 'skip'
                    self.logger.warning(f'{msg:4} {url}')
                continue

            response = self.client.get(url)

            if response.status_code == status:
                if self.SHOW_VALID:
                    self.logger.info(f'{response.status_code:4} {url}')
            else:
                self.logger.error(f'{response.status_code:4} {url}')
                errors.append({'expected': status, 'got': response.status_code, 'url': url})

        if errors:
            from pprint import pformat
            errors = pformat(errors)
            raise AssertionError(f'HTTP errors \n{errors}')
