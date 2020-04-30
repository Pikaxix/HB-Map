#-------------------------------------------------------------------------------
# Name:         manage.py.py
# Description:  
# Author:       zhnmozhang@gmail.com--EP45-DS3L
# Date:         2020/4/19  14:39
#-------------------------------------------------------------------------------
 
from app import create_app

app=create_app("development")


if __name__ == '__main__':
    app.run()