# -------------------------------------------------------------------------------
# Name:         __init__.py.py
# Description:  
# Author:       zhnmozhang@gmail.com--EP45-DS3L
# Date:         2020/3/17  23:30
# -------------------------------------------------------------------------------

from flask import Flask, make_response
from config import configs
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask_wtf import CSRFProtect
import logging
from logging.handlers import RotatingFileHandler

# DataBase
Mongodb = PyMongo()


# log config
def setupLogging(levle):
    # log level
    logging.basicConfig(level=levle)  # debug level
    # Create log handler, Set log path size limits
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # register into app
    logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    app = Flask(__name__)
    config_class = configs.get(config_name)
    app.config.from_object(config_class)
    Mongodb.init_app(app)
    setupLogging(configs[config_name].LOGGIONG_LEVEL)

    # enable CORS
    CORS(app, supports_credentials=True)

    # WTF_CSRFprotect
    # CSRFProtect(app)
    # Register BluePrint
    from app import api
    app.register_blueprint(api.api, url_prefix="/api")
    return app
