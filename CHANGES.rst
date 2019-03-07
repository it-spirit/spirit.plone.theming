Changelog
=========


1.0 (unreleased)
----------------

- Nothing changed yet.


0.9 (2019-03-07)
----------------

- Add Plone 5.2.x compatibility (Python 2.7 only).
  [tmassman]
- Drop Plone 4.2.x compatibility.
  [tmassman]
- Disable CSRF on controlpanel form due to plone.formwidget.namedfile temp storage.
  [tmassman]


0.8 (2018-01-17)
----------------

- Phone numbers starting with a '+' are getting a '00' country code prefix.
  [tmassman]
- Replace deprecated plone.directives.form with plone.supermodel to remove grok dependencies.
  [tmassman]


0.7 (2017-11-30)
----------------

- Remove 'slideshow_fullscreen' option.
  [tmassman]


0.6 (2017-10-13)
----------------

- Add snippets to show availability of theming addons.
  [tmassman]


0.5 (2017-05-18)
----------------

- Instead of providing a diazo snippet for the logo, provide a custom logo viewlet.
  [tmassman]


0.4 (2017-05-18)
----------------

- Load collective.monkeypatcher, if available, to prevent ConfigurationError.
  [tmassman]
- Add ``site_logo`` option to upload a custom site logo (Plone 4 only).
  [tmassman]


0.3 (2017-01-24)
----------------

- Add option to hide footer and colophon texts completely.
  [tmassman]
- Update installation docs and documentation images.
  [tmassman]


0.2 (2017-01-12)
----------------

- Add ``site_favicon`` option to upload a custom favicon.
  [tmassman]
- Update documentation.
  [tmassman]


0.1 (2016-12-20)
----------------

- Initial release.
  [tmassman]
