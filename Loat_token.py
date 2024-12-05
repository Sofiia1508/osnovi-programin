from dotenv import load_dotenv
import os
from decor import log_decorator
@log_decorator
def loat_token():
    load_dotenv()
    token = os.getenv('TOKEN')
    return token