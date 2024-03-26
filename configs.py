import os

class Config(object):
  LOG_CHANNEL = os.environ.get("LOG_CHANNEL",None)
  
