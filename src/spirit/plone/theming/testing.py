# -*- coding: utf-8 -*-
"""Test Layer for spirit.plone.theming."""

from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2


class Fixture(PloneSandboxLayer):
    """Custom Test Layer for spirit.plone.theming."""

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        """Set up Zope for testing."""
        # Load ZCML
        import spirit.plone.theming
        self.loadZCML(package=spirit.plone.theming)

    def setUpPloneSite(self, portal):
        """Set up a Plone site for testing."""
        applyProfile(portal, 'spirit.plone.theming:default')
        portal.portal_workflow.setDefaultChain('simple_publication_workflow')


FIXTURE = Fixture()

INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE, ),
    name='spirit.plone.theming:Integration',
)

FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE, ),
    name='spirit.plone.theming:Functional',
)

ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='spirit.plone.theming:Acceptance',
)
