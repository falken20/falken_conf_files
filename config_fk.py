# by Richi Rod AKA @richionline / falken20

"""
# Access to the file:
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config_fk import SETUP_DATA

# Load env file
load_dotenv(find_dotenv())
"""

__title__ = 'Richi Rod Portfolio'
__version__ = '1.0.0'
__author__ = 'Falken'
__url_github__ = 'https://github.com/falken20/'
__url_twitter__ = 'https://twitter.com/richionline'
__url_linkedin__ = 'https://www.linkedin.com/in/richionline/'
__license__ = 'MIT License'
__copyright__ = '© 2020 by Richi Rod AKA @richionline / falken20'
__features__ = [
]


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
