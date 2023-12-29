import os
from pathlib import Path
from dotenv import dotenv_values
basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_values(".env")

class Config(object):
    DEBUG = True

    # Development level
    DEVELOPMENT_LEVEL = os.environ.get('DEVELOPMENT_LEVEL')


app_config = {
    'config': Config
}
