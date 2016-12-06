# -*- coding: utf-8 -*-
"""Post install import steps for spirit.plone.theming."""


def post_install(context):
    """Post install script"""
    if context.readDataFile('spiritplonetheming_default.txt') is None:
        return
    # Do something during the installation of this package
