# -*- coding: utf-8 -*-
"""Test Layer for spirit.plone.theming."""

# zope imports
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
    PLONE_FIXTURE,
)
from plone.testing import (
    Layer,
    z2,
)


class Fixture(PloneSandboxLayer):
    """Custom Test Layer for spirit.plone.theming."""
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope for testing."""
        # Load ZCML
        import spirit.plone.theming
        self.loadZCML(package=spirit.plone.theming)

    def setUpPloneSite(self, portal):
        """Set up a Plone site for testing."""
        self.applyProfile(portal, 'spirit.plone.theming:default')


FIXTURE = Fixture()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE, ),
    name='spirit.plone.theming:Integration',
)

FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE, z2.ZSERVER_FIXTURE),
    name='spirit.plone.mls:Functional',
)


ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(FIXTURE, REMOTE_LIBRARY_BUNDLE_FIXTURE, z2.ZSERVER_FIXTURE),
    name='spirit.plone.mls:Acceptance',
)

ROBOT_TESTING = Layer(name='spirit.plone.mls:Robot')
