# by Richi Rod AKA @richionline / falken20

import os
from dotenv import load_dotenv, find_dotenv

# Load .env file
load_dotenv(find_dotenv())

"""
# Access to the file:
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config_fk import SETUP_DATA
"""

__title__ = 'Falken Chat'
__version__ = '1.0.0'
__author__ = 'Falken'
__url_github__ = 'https://github.com/falken20/'
__url_twitter__ = 'https://twitter.com/richionline'
__url_linkedin__ = 'https://www.linkedin.com/in/richionline/'
__license__ = 'MIT License'
__copyright__ = '© 2021 by Richi Rod AKA @richionline / falken20'
__features__ = [
]


class Config:
    # Load envioronemnt variables in .env
    TESTING = os.getenv('TESTING')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SERVER = os.getenv('SERVER')
    LOG_LEVEL = os.getenv('LOG_LEVEL')
    ENV_PRO = os.getenv('ENV_PRO')

    # Load setup data
    SETUP_DATA = {
        'title': __title__,
        'version': __version__,
        'author': __author__,
        'url_github': __url_github__,
        'url_twitter': __url_twitter__,
        'url_linkedin': __url_linkedin__,
        'license': __license__,
        'copyrigth': __copyright__,
        'features': __features__,
    }
    
# .env file
"""
SECRET_KEY=
ENV_PRO=N
LOG_LEVEL=INFO
ID_LOG=ROD->
SQLITE=N
ALLOWED_HOSTS=

# Heroku
DJANGO_SETTINGS_MODULE=covid19web.settings
"""
