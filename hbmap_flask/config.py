#-------------------------------------------------------------------------------
# Name:         config.py
# Description:  
# Author:       zhnmozhang@gmail.com--EP45-DS3L
# Date:         2020/4/19  14:46
#-------------------------------------------------------------------------------
 
import logging


class Config(object):
    # config
    SECRET_KEY = "SDUASHFIRFGHRTOHJR"
    # DataBase
    MONGO_URI = 'mongodb://HBmap_READER:DB_READER@149.129.65.236:27017/HBmap?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false'
    # MONGO_USERNAME = 'InteractDB_READER'
    # MONGO_PASSWORD = 'DB_READER'


class Development_Config(Config):
    DEBUG = True
    LOGGIONG_LEVEL = logging.DEBUG


class Production_Config(Config):
    pass


configs = {
    "development": Development_Config,
    "production": Production_Config
}