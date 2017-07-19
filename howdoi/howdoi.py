# -*- coding:utf-8 -*-
###############################
# author: niujw
# 拆轮子了 啦啦啦
# on 2017/7/19
###############################
"""
hack programmer? stay in the console and ask howdoi ?
在命令行做一些基本的编程任务.
"""

import argparse
import glob
import os
import random
import re
import requests
import requests_cache
import sys

from pygments import highliht
from pygments.lexers import guess_lexer, get_lexer_by_name
from pygments.formatters.terminal import TerminalFormatter
from pygments.util import ClassNotFound

from pyquery import PyQuery as pq
from requests.exceptions import ConnectionError
from requests.exceptions import SSLError

# 处理python2和3的引入问题
if sys.version < '3':
    import codecs
    from urllib import quote as url_quote
    from urllib import getproxies
    def u(x):#处理unicode
       return codecs.unicode_escape_decode(x)[0]
else:
    
    from urllib.request import getproxies
    from urllib.parse import quote as url_quote

    def u(x):
        return x

if os.getenv('HOWDOI_DISABLE_SSL'):
    SEARCH_URL = 'http://www.google.com/search?q=site:{0}%20{1}'
    VERIFY_SSL_CERTIFICATE = False
else:
    SEARCH_URL = 'http://www.google.com/search?q=site:{0}%20{1}'
    VERIFY_SSL_CERTIFICATE = False
URL = os.getenv('HOWDOI_URL') or 'stackoverflow.com'
USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
               'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
               ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) '
                'Chrome/19.0.1084.46 Safari/536.5'),
               ('Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46'
                'Safari/536.5'), ) 
ANSWER_HEADER = u('--- Answer {0} ---\n{1}')
NO_ANSWER_MSG = '< no answer given >'
XDG_CACHE_DIR = os.environ.get('XDG_CACHE_HOME', os.path.join(os.path.expanduser('~'), '.cache'))
CACHE_DIR = os.path.join(XDG_CACHE_DIR, 'howdoi')
CACHE_FILE = os.path.join(CACHE_DIR, 'cache{0}'.format(sys.version_info[0] if sys.version_info[0] if sys.version_info[0] == 3 else ''))
