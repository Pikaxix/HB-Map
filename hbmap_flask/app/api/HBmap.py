#-------------------------------------------------------------------------------
# Name:         HBmap.py
# Description:  
# Author:       zhnmozhang@gmail.com--EP45-DS3L
# Date:         2020/4/19  20:32
#-------------------------------------------------------------------------------
 
from . import api
from . import Mongodb
from flask import jsonify,request

@api.route("/bodysites",methods=['GET'])
def systems():
    """GET system view"""
    find = Mongodb.db.bodysites.find()
    result = []
    total_num = 0
    for it in find:
        total_num += it['num']
        result.append({
            'id' : str(it['_id']),
            'site': it['site'],
            'disease': it['disease'],
            'normal': it['num'],
            'abnormal': 35
            })
    return jsonify({
        "bodysites" : result,
        "total_sum" : total_num
    })