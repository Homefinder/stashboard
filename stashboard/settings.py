import os

DEBUG = False

SITE_NAME = "Statusboard"
SITE_AUTHOR = "Colonel Mustache"
SITE_URL = "http://hfstatus.appspot.com"
REPORT_URL = "mailto:help@homefinder.com"

# Twitter update settings
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET = ''
TWITTER_HANDLE = ''

# Hipchat settings
HIPCHAT_API_KEY = ''
HIPCHAT_ROOM_ID = ''

# RSS Feed settings
RSS_NUM_EVENTS_TO_FETCH = 50

# OAuth Consumer Credentials
CONSUMER_KEY = 'anonymous'
CONSUMER_SECRET = 'anonymous'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
    )
