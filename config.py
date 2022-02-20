import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'OI_SHR%$CV__23#+_sdefoqA'