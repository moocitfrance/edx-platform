# -*- coding: utf-8 -*-
"""
Settings for Bok Choy tests that are used when running Studio in Docker-based devstack.
"""

# noinspection PyUnresolvedReferences
from .bok_choy import *  # pylint: disable=wildcard-import

CMS_BASE = '{}:{}'.format(os.environ['BOK_CHOY_HOSTNAME'], os.environ['BOK_CHOY_CMS_PORT'])
LMS_BASE = '{}:{}'.format(os.environ['BOK_CHOY_HOSTNAME'], os.environ['BOK_CHOY_LMS_PORT'])
LMS_ROOT_URL = 'http://{}'.format(LMS_BASE)

COMMENTS_SERVICE_URL = 'http://{}:4567'.format(os.environ['BOK_CHOY_HOSTNAME'])
EDXNOTES_PUBLIC_API = 'http://{}:8042/api/v1'.format(os.environ['BOK_CHOY_HOSTNAME'])

# Docker does not support the syslog socket at /dev/log. Rely on the console.
LOGGING['handlers']['local'] = LOGGING['handlers']['tracking'] = {
    'class': 'logging.NullHandler',
}

LOGGING['loggers']['tracking']['handlers'] = ['console']

# Point the URL used to test YouTube availability to our stub YouTube server
BOK_CHOY_HOST = os.environ['BOK_CHOY_HOSTNAME']
YOUTUBE['API'] = "http://{}:{}/get_youtube_api/".format(BOK_CHOY_HOST, YOUTUBE_PORT)
YOUTUBE['METADATA_URL'] = "http://{}:{}/test_youtube/".format(BOK_CHOY_HOST, YOUTUBE_PORT)
YOUTUBE['TEXT_API']['url'] = "{}:{}/test_transcripts_youtube/".format(BOK_CHOY_HOST, YOUTUBE_PORT)
