import hashlib
import hmac
import json
import os

from django.http import HttpResponse
from django.views.decorators import http

from .actions import deploying


@http.require_POST
def deploy(request):
    # check if the given signature of X_HUB_SIGNATURE matches 'sha1=' + hash
    # make sure to use a secure co
    expected = request.META.get('HTTP_X_HUB_SIGNATURE')
    hashed = 'sha1=' + hmac.new(os.environ.get('X_HUB_SIGNATURE').encode('utf-8'), request.body, hashlib.sha1).hexdigest()
    if hmac.compare_digest(expected, hashed):
        deploying.deploy_project()
        return HttpResponse()
    return HttpResponse(status=403)
