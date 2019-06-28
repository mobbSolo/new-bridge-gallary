#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'markie_tee'
SITENAME = 'The New Bridge Gallary'
SITEURL = ''

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['img', 'pdf']

TIMEZONE = 'America/Denver'
DEFAULT_LANG = 'en'

THEME = 'theme'

PLUGIN_PATHS = ['plugins/', ]

PLUGINS = ['i18n_subsites',
            'liquid_tags',
            'pelican-bootstrapify',
]

BOOTSTRAP_THEME = 'flatly'

PYGMENTS_STYLE = 'monokai'

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
LINKS = (('Raitman Art', 'https://www.raitmanart.com/'),
         ('The Mitchell Gallary', 'https://www.mitchellcontemporary.com/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
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
