# Go to the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
  pass
  
except Exception as err:
    logging.error(f'{os.getenv("ID_LOG", "")} Error in method create_list_urls \n'
                  f'Line: {err.__traceback__.tb_lineno} \n'
                  f'File: {err.__traceback__.tb_frame.f_code.co_filename} \n'
                  f'Type Error: {type(err).__name__} \n'
                  f'Arguments:\n {err.args}')
    raise
