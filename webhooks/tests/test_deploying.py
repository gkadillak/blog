from unittest import mock
import subprocess
from django.test import TestCase

import logging

from webhooks.actions import deploying


class TestDeploying(TestCase):

    def test_exception_raises_right_context(self):
        with mock.patch('webhooks.actions.deploying.restart_gunicorn') as mock_subprocess:
            mock_subprocess.side_effect = subprocess.CalledProcessError(returncode=2, cmd=['blah'], output='hey there')
            with self.assertRaises(subprocess.CalledProcessError):
                deploying.restart_gunicorn()

