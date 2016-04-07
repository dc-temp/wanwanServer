# coding=utf-8
import sqlite3

class DBCursor:
    '''自定义游标对象'''

    def __init__(self,conn):
        '''
        @param conn: conn 数据库连接对象
        '''
        self.conn = conn
        self.cursor = conn.cursor()

    def execute(self,sql):
        '''语句执行
        @param sql: str sql 语句
        '''
        count = self.cursor.execute(sql)
        return count

    def executemany(self,sql,args):
        '''语句执行
        @param sql: str sql 语句
        '''
        count = self.cursor.executemany(sql,args)
        return count

    def fetchall(self):
        '''获取所有游标对象中的数据'''
        return self.cursor.fetchall()

    def fetchone(self):
        '''获取所有游标对象中的一条数据'''
        return self.cursor.fetchone()

    def close(self):
        '''删除游标对象'''
        self.cursor.close()
        self.conn.close()

class DBManager:
    '''数据库管理'''
    def __init__(self, name):
        self.name = name

    def get(self):
        conn = sqlite3.connect(self.name)
        conn.isolation_level = None
        return conn

    def cursor(self):
        conn = self.get()
        cur = DBCursor(conn)
        return cur

