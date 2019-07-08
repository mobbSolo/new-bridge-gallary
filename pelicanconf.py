#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'New Bridge Art'
SITENAME = 'The New Bridge Gallary'
SITEURL = ''

TIMEZONE = 'America/Denver'
DEFAULT_LANG = 'en'

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['img', 'pdf']
PLUGIN_PATHS = ['plugins/', ]

PLUGINS = ['i18n_subsites',
            'jinja2content',
            'photos',
]

THEME = 'pelican-bootstrap3/'

BOOTSTRAP_THEME = 'flatly'
PHOTO_LIBRARY = "~/dev/nb_photos"

PYGMENTS_STYLE = 'monokai'

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

# Blogroll
LINKS = (('Glenwood Hot Springs', 'https://www.hotspringspool.com'),
         ('Hotel Colorado', 'https://www.hotelcolorado.com/'),
         ('Brew Garden', 'https://www.glenwoodspringsbrewgarden.com/'),
)

# Social widget
SOCIAL = (('Instagram', 'https://www.instagram.com/newbridgeart/?igshid=14s7ehw1k5syo'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'

# DEFAULT_METADATA = {
    # 'Author': 'Markie Tee',
    # 'Category': 'testing',
# }

#FAVICON = ('img/eye-tri_32-alpha.png')
