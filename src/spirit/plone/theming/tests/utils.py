# -*- coding: utf-8 -*-
"""Utilities for setting up test content."""

# python imports
from datetime import (
    datetime,
    timedelta,
)
from tzlocal import get_localzone
import pkg_resources

# zope imports
from DateTime import DateTime
from plone import api

# local imports
from spirit.plone.theming import logger

TZNAME = get_localzone().zone
DUMMY_TEXT_SHORT = """Lorem ipsum dolor sit amet, consetetur sadipscing elitr,
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam
erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea
rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum
dolor sit amet."""
DUMMY_TEXT = """<p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr,
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam
erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea
rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum
dolor sit amet.</p>\n<p>Lorem ipsum dolor sit amet, consetetur sadipscing
elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna
aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo
dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est
Lorem ipsum dolor sit amet.</p>\n<p>Lorem ipsum dolor sit amet, consetetur
sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore
magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo
dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est
Lorem ipsum dolor sit amet. Duis autem vel eum iriure dolor in hendrerit in
vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla
facilisis at vero eros et accumsan et iusto odio dignissim qui blandit
praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi.
Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy
nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi
enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis
nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in
hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu
feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui
blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla
facilisi.</p>\n<p>Nam liber tempor cum soluta nobis eleifend option congue
nihil imperdiet doming id quod mazim placerat facer possim assum. Lorem ipsum
dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod
tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad
minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl
ut aliquip ex ea commodo consequat.</p>"""


def setup_plone_content(context):
    """Add test plone content."""
    portal = _get_navigation_root(context)

    create_event_items(portal)
    create_news_items(portal)


def setup_add_ons(context):
    """Configure add-ons and add test content."""
    portal = _get_navigation_root(context)

    configure_collective_cover(context)

    create_products_carousel_content(portal)
    create_products_doormat_content(portal)
    create_products_ploneformgen_content(portal)
    create_collective_cover_content(portal)


def configure_collective_cover(context):
    """Add sample configuration for collective.cover."""


def create_event_items(portal):
    """Create sample event items."""
    events = portal.get('events')
    if not events:
        events = api.content.create(
            container=portal,
            type='Folder',
            id='events',
            title=u'Events',
            description=u'This folder was created for testing purposes',
        )

    for i in xrange(25):
        content_id = 'example-event-item-{0}'.format(i)
        if not events.get(content_id):
            today = datetime.today() + timedelta(days=i)
            tomorrow = today + timedelta(days=1)
            content = api.content.create(
                type='Event',
                container=events,
                description=DUMMY_TEXT_SHORT,
                end=tomorrow,  # Dexterity
                endDate=DateTime(tomorrow),  # Archetypes
                id=content_id,
                start=today,  # Dexterity
                startDate=DateTime(today),  # Archetypes
                timezone=TZNAME,
                title=u'Example event no. {0}'.format(i),
            )
            set_text_field(content, DUMMY_TEXT)
            _publish(content)
            content.reindexObject()


def create_news_items(portal):
    """Create sample news items."""

    news = portal.get('news')
    if not news:
        news = api.content.create(
            container=portal,
            type='Folder',
            id='news',
            title=u'News',
            description=u'This folder was created for testing purposes',
        )

    for i in xrange(25):
        content_id = 'example-news-item-{0}'.format(i)
        if not news.get(content_id):
            content = api.content.create(
                type='News Item',
                container=news,
                description=DUMMY_TEXT_SHORT,
                id=content_id,
                title=u'Example news item no. {0}'.format(i),
            )
            set_text_field(content, DUMMY_TEXT)
            _publish(content)
            content.reindexObject()


def create_products_carousel_content(portal):
    """Create sample Products.Carousel content."""


def create_products_doormat_content(portal):
    """Create sample Products.Doormat content."""
    try:
        pkg_resources.get_distribution('Products.Doormat')
    except pkg_resources.DistributionNotFound:
        logger.info('Products.Doormat is not available.')
        return

    sample_doormat = portal.get('doormat')
    if sample_doormat:
        api.content.delete(sample_doormat)

    content_id = 'example-doormat'
    content = portal.get(content_id)
    if content:
        return

    doormat = api.content.create(
        type='Doormat',
        container=portal,
        id=content_id,
        title=u'Example doormat',
    )
    doormat.setExcludeFromNav(True)

    # Create 4 columns
    for i in xrange(4):
        column_no = i + 1
        column = api.content.create(
            type='DoormatColumn',
            container=doormat,
            id='column-{0}'.format(column_no),
            title=u'Column {0}'.format(column_no),
        )
        section = api.content.create(
            type='DoormatSection',
            container=column,
            id='section-{0}-1'.format(column_no),
            title=u'Section {0}-1'.format(column_no),
        )
        document = api.content.create(
            type='Document',
            container=section,
            id='page-{0}-1-1'.format(column_no),
            title=u'Page {0}-1-1'.format(column_no),
        )
        set_text_field(document, u'<p>{0}</p>'.format(DUMMY_TEXT_SHORT))

        _publish(document)
        document.reindexObject()

        _publish(section)
        section.reindexObject()

        _publish(column)
        column.reindexObject()

    _publish(doormat)
    doormat.reindexObject()


def create_products_ploneformgen_content(portal):
    """Create sample Products.PloneFormGen content."""


def create_collective_cover_content(portal):
    """Create sample collective.cover content items."""


def set_text_field(obj, text):
    """Set text field in object on both, Archetypes and Dexterity."""
    from plone.app.textfield.value import RichTextValue
    try:
        obj.setText(text)  # Archetypes
    except AttributeError:
        obj.text = RichTextValue(text, 'text/html', 'text/html')  # Dexterity
    finally:
        obj.reindexObject()


def _publish(content):
    """Publish the object if it hasn't been published."""
    if api.content.get_state(obj=content) != 'published':
        api.content.transition(obj=content, transition='publish')
        return True
    return False


def _get_navigation_root(context):
    """Find the correct navigation root."""
    documents = api.content.find(portal_type='Document', id='front-page')
    if len(documents) == 0:
        return api.portal.get()
    front_page = documents[0].getObject()

    return api.portal.get_navigation_root(front_page)
