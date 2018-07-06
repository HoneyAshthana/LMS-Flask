"""import logging
from logging.handlers import RotatingFileHandler

from api import app"""
#logging
"""handler = RotatingFileHandler('history.log', maxBytes=100000, backupCount=1)
#handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setLevel(logging.ERROR) formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
app.logger.addHandler(handler)"""
"""
formatter = logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
handler = RotatingFileHandler('history.log', maxBytes=10000000, backupCount=5)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
app.logger.addHandler(handler)"""
"""
from logging import WARNING, FileHandler
from api import app

file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)
app.logger.addHandler(file_handler)
"""