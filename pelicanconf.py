#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Python Nairobi'
SITENAME = u'#PyNBO'
SITEURL = u'http://blog.pynbo.or.ke'
TAGLINE = u'The Python-Nairobi Blog'

PATH = 'content'

TIMEZONE = 'Africa/Nairobi'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('PyNBO Meetup', 'http://meetup.com/Python-Nairobi/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True 

# global metadata to all the contents
#DEFAULT_METADATA = (('key', 'val'),)

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    }

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'img',
    'js',
    'css',
    'skulpt',
    'extra/robots.txt',
    'CNAME',
    ]

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}
GITHUB_URL = "http://github.com/kili/help.kili.io"
#DISQUS_SITENAME = ""
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 4
DEFAULT_DATE = (1969, 12, 31, 23, 59, 59) 
THEME = "pure-pynbo"
HIDE_SIDEBAR = True
CUSTOM_CSS = 'css/pynbo.css'
SHOW_ARTICLE_AUTHOR = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_ARCHIVES_ON_MENU = False
DEFAULT_DATE_FORMAT = ('%B %d, %Y')
COVER_IMG_URL = 'img/blog-bg.png'
PAGE_EXCLUDES = ['.git']
IGNORE_FILES = ['*.swp','.git*']
