# -*- coding: utf-8 -*-
"""Vocabularies used by spirit.plone.theming."""

from plone import api as ploneapi
from plone.api.exc import InvalidParameterError
from plone.registry.interfaces import IRegistry
from spirit.plone.theming import _
from spirit.plone.theming.interfaces import IPloneThemingVocabularies
from zope.component import getUtility
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class BaseVocabulary(object):
    """A base vocabulary class."""

    def _get_registry_record(self, name=None):
        try:
            return ploneapi.portal.get_registry_record(
                name=name,
                interface=IPloneThemingVocabularies,
            )
        except InvalidParameterError:
            return
        except KeyError:
            registry = getUtility(IRegistry)
            registry.registerInterface(IPloneThemingVocabularies)
            try:
                return ploneapi.portal.get_registry_record(
                    name=name,
                    interface=IPloneThemingVocabularies,
                )
            except (KeyError, InvalidParameterError):
                ploneapi.portal.show_message(
                    message=_(
                        u'Please upgrade or reinstall spirit.plone.theming'
                    ),
                    request=getRequest(),
                )
                return


@implementer(IVocabularyFactory)
class AvailableHeaderOptionsVocabulary(BaseVocabulary):
    """Vocabulary for available header options."""

    def __call__(self, context):

        options = self._get_registry_record(name='available_header_options')

        items = [SimpleTerm(value=i, title=i) for i in sorted(options)]
        return SimpleVocabulary(items)


@implementer(IVocabularyFactory)
class AvailableFooterOptionsVocabulary(BaseVocabulary):
    """Vocabulary for available footer options."""

    def __call__(self, context):

        options = self._get_registry_record(name='available_footer_options')

        items = [SimpleTerm(value=i, title=i) for i in sorted(options)]
        return SimpleVocabulary(items)


@implementer(IVocabularyFactory)
class AvailableColorOptionsVocabulary(BaseVocabulary):
    """Vocabulary for available color options."""

    def __call__(self, context):

        options = self._get_registry_record(name='available_color_options')

        items = [SimpleTerm(value=i, title=i) for i in sorted(options)]
        return SimpleVocabulary(items)


@implementer(IVocabularyFactory)
class AvailablePatternOptionsVocabulary(BaseVocabulary):
    """Vocabulary for available pattern options."""

    def __call__(self, context):

        options = self._get_registry_record(name='available_pattern_options')

        items = [SimpleTerm(value=i, title=i) for i in sorted(options)]
        return SimpleVocabulary(items)


@implementer(IVocabularyFactory)
class AvailableLayoutOptionsVocabulary(BaseVocabulary):
    """Vocabulary for available layout options."""

    def __call__(self, context):

        options = self._get_registry_record(name='available_layout_options')

        items = [SimpleTerm(value=i, title=i) for i in sorted(options)]
        return SimpleVocabulary(items)
