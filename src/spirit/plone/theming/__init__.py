# -*- coding: utf-8 -*-
"""Theming extensions for Plone Websites."""

from plone import api as ploneapi
from spirit.plone.theming import config
from zope.i18nmessageid import MessageFactory

import logging


PLONE_4 = '4' <= ploneapi.env.plone_version() < '5'
PLONE_5 = '5' <= ploneapi.env.plone_version() < '6'

logger = logging.getLogger(config.PROJECT_NAME)
_ = MessageFactory('spirit.plone.theming')
