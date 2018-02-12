import json
import os

from unittest import mock, skip
from django.test import TestCase, Client



class ViewsTest(TestCase):

    @skip('figuring out hash')
    @mock.patch("webhooks.views.deploying.deploy_project")
    def test_post_request_for_merged_pull_request(self, mock_deploy_project):
        with open(os.getcwd() + '/webhooks/tests/fixtures/successful_merge_event.json') as json_file:
            with mock.patch("webhooks.views.os.environ", {"X_HUB_SIGNATURE": "somedumbkey"}):
                client = Client()
                response = client.post('/webhooks/deploy',
                                       data=json_file.read(),
                                       content_type="application/json",
                                       HTTP_X_HUB_SIGNATURE="sha1=somedumbhash")
                self.assertEqual(mock_deploy_project.call_count, 1)
                self.assertEqual(response.status_code, 200)

    @skip('figuring out hash')
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
    def test_environmental_variables_not_set(self, mock_deploy_project):
        with mock.patch("webhooks.views.os.environ", {"X_HUB_SIGNATURE": "NOPE"}):
            client = Client()
            response = client.post('/webhooks/deploy',
                                   content_type="application/json")
            self.assertEqual(mock_deploy_project.call_count, 0)
            self.assertEqual(response.status_code, 403)


    @mock.patch("webhooks.views.deploying.deploy_project")
    def test_header_not_sent(self, mock_deploy_project):
        client = Client()
        response = client.post('/webhooks/deploy',
                               content_type="application/json",
                               HTTP_X_HUB_SIGNATURE="PARTY-PLAZA")
        self.assertEqual(mock_deploy_project.call_count, 0)
        self.assertEqual(response.status_code, 403)

