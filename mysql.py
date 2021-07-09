#!/usr/bin/python3

import pymysql

class SqlFunc():
    def __init__(self):
        # 打开数据库连接
        self.db = pymysql.connect(host="198.13.47.120", user="shop", password="fEh63JddcZR3LYLM", database="shop")
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        self.cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 方法获取单条数据.
        data = self.cursor.fetchone()
        print("Database version : %s " % data)

    def select(self,sql):
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 获取所有记录列表
            results = self.cursor.fetchall()
            return results
        except:
            print("Error: unable to fetch data")
            return None

    def update(self,sql):
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

    def insert(self,sql):
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()

    def __del__(self):
        self.db.close()

