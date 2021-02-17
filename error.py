# Print logs using colors
from rich import print
print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())

# Go to the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set the format of logging messages
logging.basicConfig(format=f'{os.getenv("ID_LOG", "")} %(levelname)s:%(asctime)s: '
                           f'File: %(filename)s: Function: %(funcName)s\n'
                           '%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=os.getenv("LOG_LEVEL", "INFO"))

try:
  pass
  
except Exception as err:
    logging.error(f'Line: {err.__traceback__.tb_lineno} \n'
                  f'File: {err.__traceback__.tb_frame.f_code.co_filename} \n'
                  f'Type Error: {type(err).__name__} \n'
                  f'Arguments:\n {err.args} \n'
                  f'Error:\n {format(err)}')
    raise
