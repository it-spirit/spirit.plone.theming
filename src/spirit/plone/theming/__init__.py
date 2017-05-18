# -*- coding: utf-8 -*-
"""Theming extensions for Plone Websites."""

# python imports
import logging

# zope imports
from plone import api as ploneapi
from zope.i18nmessageid import MessageFactory

# local imports
from spirit.plone.theming import config


PLONE_4 = '4' <= ploneapi.env.plone_version() < '5'
PLONE_5 = '5' <= ploneapi.env.plone_version() < '6'

logger = logging.getLogger(config.PROJECT_NAME)
_ = MessageFactory('spirit.plone.theming')
