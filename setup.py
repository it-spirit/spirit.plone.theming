# -*- coding: utf-8 -*-
"""Setup for spirit.plone.theming package."""

from setuptools import (
    find_packages,
    setup,
)

version = '0.1'
description = "Theming extensions for Plone Websites."
long_description = ('\n'.join([
    open('README.rst').read(),
    'Contributors',
    '------------\n',
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
]))


install_requires = [
    'setuptools',
    # -*- Extra requirements: -*-
    'collective.themesitesetup',
    'plone.api',
    'plone.app.registry',
    'plone.directives.form',
    'tzlocal',
]

setup(
    name='spirit.plone.theming',
    version=version,
    description=description,
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='plone zope theming',
    author='it-spirit',
    author_email='thomas.massmann@it-spir.it',
    url='https://github.com/it-spirit/spirit.plone.theming',
    download_url='http://pypi.python.org/pypi/spirit.plone.theming',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['spirit', 'spirit.plone'],
    include_package_data=True,
    zip_safe=False,
    extras_require=dict(
        test=[
            'plone.app.layout[test]',
            'plone.app.robotframework[debug]',
            'plone.app.testing',
            'plone.app.textfield',
            'plone.namedfile',
            'robotframework-selenium2screenshots',
        ],
    ),
    install_requires=install_requires,
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """,
)
