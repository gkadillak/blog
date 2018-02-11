import json
import os

from unittest import mock
from django.test import TestCase, Client



class ViewsTest(TestCase):

    @mock.patch("webhooks.views.deploying.deploy_project")
    def test_post_request_for_merged_pull_request(self, mock_deploy_project):
        with open(os.getcwd() + '/webhooks/tests/fixtures/successful_merge_event.json') as json_file:
            with mock.patch("webhooks.views.os.environ", {"X_HUB_SIGNATURE": "PARTY-PLAZA"}):
                client = Client()
                response = client.post('/webhooks/deploy',
                                       data=json_file.read(),
                                       content_type="application/json",
                                       HTTP_X_HUB_SIGNATURE="PARTY-PLAZA")
                self.assertEqual(mock_deploy_project.call_count, 1)
                self.assertEqual(response.status_code, 200)

    @mock.patch("webhooks.views.deploying.deploy_project")
    def test_post_request_for_closed_pull_request(self, mock_deploy_project):
        with open(os.getcwd() + '/webhooks/tests/fixtures/unsuccessful_merge_event.json') as json_file:
            with mock.patch("webhooks.views.os.environ", {"X_HUB_SIGNATURE": "PARTY-PLAZA"}):
                client = Client()
                response = client.post('/webhooks/deploy',
                                       data=json_file.read(),
                                       content_type="application/json",
                                       HTTP_X_HUB_SIGNATURE="PARTY-PLAZA")
                self.assertEqual(mock_deploy_project.call_count, 0)
                self.assertEqual(response.status_code, 200)


    @mock.patch("webhooks.views.deploying.deploy_project")
    def test_signature_does_not_match(self, mock_deploy_project):
        with mock.patch("webhooks.views.os.environ", {"X_HUB_SIGNATURE": "NOPE"}):
            client = Client()
            response = client.post('/webhooks/deploy',
                                   content_type="application/json",
                                   HTTP_X_HUB_SIGNATURE="YES")
            self.assertEqual(mock_deploy_project.call_count, 0)
            self.assertEqual(response.status_code, 200)


