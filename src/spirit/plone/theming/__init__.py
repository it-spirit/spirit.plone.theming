# -*- coding: utf-8 -*-
"""Theming extensions for Plone Websites."""

# python imports
import logging

# zope imports
from zope.i18nmessageid import MessageFactory

# local imports
from spirit.plone.theming import config

logger = logging.getLogger(config.PROJECT_NAME)
_ = MessageFactory('spirit.plone.theming')
