import json
import os

from django.http import HttpResponse
from django.views.decorators import http

from .actions import deploying


@http.require_POST
def deploy(request):
    http_response = HttpResponse('OK')

    if request.META.get("HTTP_X_HUB_SIGNATURE") != os.environ.get("X_HUB_SIGNATURE"):
        return http_response

    decoded_body = request.body.decode('utf-8')
    body = json.loads(decoded_body)
    pull_request = body.get('pull_request')
    is_merged = pull_request.get('state') == 'closed' and body.get('pull_request').get('merged')
    is_master = pull_request.get('base').get('ref') == 'master'

    if is_merged and is_master:
        deploying.deploy_project()
    return http_response
