#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Daniel P Russo'
SITENAME = u'DeLorean - They Drew First Blog'
SITEURL = 'https://russodanielp.github.io/'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
ASSET_SOURCE_PATHS = ['theme'] # changed this as per https://github.com/getpelican/pelican/issues/1523
# Blogroll
LINKS = (('Zhu Research Group', 'http://zhu.camden.rutgers.edu/'),
         ('Rutgers Center for Computational and Integrative Biology', 'https://ccib.camden.rutgers.edu/')
         )

# Social widget
SOCIAL = [('@russodanielp', 'https://twitter.com/russodanielp')]

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
