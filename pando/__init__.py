"""
.. automodule:: pando.body_parsers
.. automodule:: pando.exceptions
.. automodule:: pando.http
.. automodule:: pando.logging
.. automodule:: pando.state_chain
.. automodule:: pando.testing
.. automodule:: pando.utils
.. automodule:: pando.website
.. automodule:: pando.wsgi

"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from os.path import dirname, join
import sys
import pkg_resources

import aspen.utils as _x  # this registers the 'repr' codec error strategy
del _x

# imports of convenience
from aspen.simplates import json_ as json
from aspen.simplates.renderers import BUILTIN_RENDERERS, RENDERERS
from .http.response import Response
from .logging import log, log_dammit

# Shut up, PyFlakes. I know I'm addicted to you.
Response, json, log, log_dammit, BUILTIN_RENDERERS, RENDERERS

try:
    dist = pkg_resources.get_distribution('pando')
    __version__ = dist.version
except pkg_resources.DistributionNotFound:
    with open(join(dirname(dirname(__file__)), 'version.txt')) as f:
        __version__ = f.read()

WINDOWS = sys.platform[:3] == 'win'

is_callable = callable

