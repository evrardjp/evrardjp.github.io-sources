#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jean-Philippe Evrard'
AUTHOR_GENERIC_USERNAME = 'evrardjp'
SITENAME = u'dd if=/dev/brain of=this.site'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
        )

# Social widget
LINKEDIN_USER = AUTHOR_GENERIC_USERNAME
LINKEDIN_URL = 'https://www.linkedin.com/in/' + LINKEDIN_USER
GITHUB_URL = 'https://github.com/' + AUTHOR_GENERIC_USERNAME
SOCIAL = (('LinkedIn', LINKEDIN_URL),
          ('Github', GITHUB_URL),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'pdfs','extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


#THEME = 'themes/twenty-pelican-html5up'
#ABOUT_TEXT = 'TODO!'
#ABOUT_IMAGE = TODO
#ABOUT_LINK = TODO
COPYRIGHT = AUTHOR
#SHOW_COPYRIGHT : True by default, you can set it to False to hide the copyrights.