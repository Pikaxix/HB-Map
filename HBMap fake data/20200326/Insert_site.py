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
    conn = MongoClient(
        "mongodb://HBmap_ADMIN:DB_ADMIN@149.129.65.236:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
    db = conn.HBmap
    collect = db.bodysites
    #初始化Socket参数 数据库 集合

    collect.remove(None)
    #第二种remove不好用的时候
    # set1.delete_many({})
    return collect


def insertToMongoDB(collect):
    # 打开文件
    with open('./假数据对照表disease-bodySite.csv', 'r', encoding=' utf-8-sig')as csvfile:
        reader = csv.DictReader(csvfile)
        cnt = 0
        sum=0
        # 创建一个counts计数一下 看自己一共添加了了多少条数据
        insert_list=[]
        for each in reader:
            # print(each)
            item = {}
            item['site'] = each['body site']
            item['disease'] = each['disease']
            item['num'] = int(each['n'])
           
           #print(item)
            insert_list.append(item)
            cnt += 1
            if(cnt == 100):
                print(str(cnt) + " records has been found")
                try:
                    print("Inserting......")
                    collect.insert_many(insert_list)
                    insert_list.clear()
                    print(str(cnt) + " records has been insterted.")
                    sum += cnt
                    cnt = 0
                finally:
                    print("A total of " + str(sum) +
                          " records has been inserted.\n")
    if(cnt != 0):
        print(str(cnt) + " records has been found")
        try:
            print("Inserting......")
            collect.insert_many(insert_list)
            insert_list.clear()
            print(str(cnt) + " records has been insterted.")
            sum += cnt
            cnt = 0
        finally:
            print("A total of " + str(sum) + " records has been inserted.\n")

    print("Insert completed!\n")


def main():
    collect = connection()
    insertToMongoDB(collect)


if __name__ == '__main__':
    main()
