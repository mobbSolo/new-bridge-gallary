#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

LOAD_CONTENT_CACHE = False
AUTHOR = 'New Bridge Art'
SITENAME = 'The New Bridge Gallary'
SITELOGO = 'img/new_bridge_small.gif'
FAVICON = 'img/favicon.gif'
SITELOGO_SIZE = 125
HIDE_SITENAME = True

# Add custom CSS overrides sitewide
CUSTOM_CSS = 'static/css/custom.css'
GOOGLE_WEBFONTS = 'Raleway:light,extralight,bold'
GOOGLE_VARIFY = os.environ['GOOGLE_SEARCH_VARIFY']

TIMEZONE = 'America/Denver'
DEFAULT_LANG = 'en'

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
# Tell Pelican to add files from here to the output dir
STATIC_PATHS = ['img', 'extra']
# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
}
PLUGIN_PATHS = ['plugins/', ]
PLUGINS = ['i18n_subsites',
            'jinja2content',
            'photos',
]

THEME = 'pelican-bootstrap3/'
SIDEBAR_ON_LEFT = False
BOOTSTRAP_THEME = 'yeti'
PADDED_SINGLE_COLUMN_STYLE = False
DISPLAY_CATEGORIES_ON_MENU = False

# photo plugin ========================
PHOTO_LIBRARY = "~/dev/nb_photos"
PHOTO_ARTICLE = (760, 506, 80)
PHOTO_SQUARE_THUMB = False
PHOTO_RESIZE_JOBS = 3
PHOTO_WATERMARK = True
PHOTO_WATERMARK_TEXT = "New Bridge Art"
PHOTO_EXIF_COPYRIGHT = 'COPYRIGHT'
# =====================================


JINJA2CONTENT_TEMPLATES = ['jinja_temp']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS_WIDGET_NAME = 'Friends'
# Blogroll
LINKS = (('Glenwood Hot Springs', 'https://www.hotspringspool.com'),
         ('Hotel Colorado', 'https://www.hotelcolorado.com/'),
         ('Brew Garden', 'https://www.glenwoodspringsbrewgarden.com/'),
         ('Painters Stage Music', 'https://thebash.com/dance-band/painters-stage'),
)

# Social widget
SOCIAL = (('Instagram', 'https://www.instagram.com/newbridgeart/?igshid=14s7ehw1k5syo'),
        # ('Bandcamp', 'https://paintersstage.bandcamp.com'),
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}.html'

#FAVICON = ('img/eye-tri_32-alpha.png')

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

# MENUITEMS = ()
