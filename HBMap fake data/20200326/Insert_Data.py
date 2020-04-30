#-*- coding:utf-8 -*- -

# @Create_Time   : 2020年2月28日
# @Modify_Time   : 2020年3月24日
# @Author  : Zhnmozhang@Gmail.com
# @Site   :
# @File   : csv文件存入mongoDB.py
# @Environment  : VS Code Python --3.8.2

from pymongo import MongoClient
import csv
import re


def connection():
    conn = MongoClient("149.129.65.236:27017")
    db = conn.HBMAP
    collect = db.sites
    #初始化Socket参数 数据库 集合

    collect.remove(None)
    #第二种remove不好用的时候
    # set1.delete_many({})
    return collect


def insertToMongoDB(collect):
    # 打开文件
    with open('./bodySite.csv', 'r', encoding=' utf-8-sig')as csvfile:
        reader = csv.DictReader(csvfile)
        cnt = 0
        # 创建一个counts计数一下 看自己一共添加了了多少条数据
        insertlist=[]
        for each in reader:
            # print(each)
            item = {}
            item['disease'] = each['disease']
            item['site'] = each['body site']
            item['num'] = each['n']
            print(item)
            insertlist.append(item)
            cnt += 1
        print(str(cnt) + "records has been found\n")
            

        try:
            print ("Inserting......\n")
        finally:
            print("Insert completed!\n")


def main():
    collect = connection()
    insertToMongoDB(collect)


if __name__ == '__main__':
    main()
