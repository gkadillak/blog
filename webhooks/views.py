import hashlib
import hmac
import json
import os

from django.http import HttpResponse
from django.views.decorators import http

from .actions import deploying
import logging

logger = logging.getLogger(__name__)


@http.require_POST
def deploy(request):
    # check if the given signature of X_HUB_SIGNATURE matches 'sha1=' + hash
    # make sure to use a secure co
    if not request.META.get('HTTP_X_HUB_SIGNATURE'):
        logger.error('HTTP_X_HUB_SIGNATURE required but not given')
        return HttpResponse(status=403)
    if not os.environ.get('X_HUB_SIGNATURE'):
        logger.error('X_HUB_SIGNATURE required but not given')
        return HttpResponse(status=403)

    expected = request.META.get('HTTP_X_HUB_SIGNATURE')
    hashed = 'sha1=' + hmac.new(os.environ.get('X_HUB_SIGNATURE').encode('utf-8'), request.body, hashlib.sha1).hexdigest()
    if hmac.compare_digest(expected, hashed):
        deploying.deploy_project()
        return HttpResponse()
    return HttpResponse(status=403)
