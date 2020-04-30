#-------------------------------------------------------------------------------
# Name:         __init__.py.py
# Description:  
# Author:       zhnmozhang@gmail.com--EP45-DS3L
# Date:         2020/4/19  14:38
#-------------------------------------------------------------------------------

from flask import Blueprint
from app import Mongodb


# create Blueprint object
api = Blueprint("api",__name__)

# resister Blueprint modules
from . import  demo
from . import HBmap