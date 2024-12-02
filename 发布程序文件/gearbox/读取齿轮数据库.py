# -*- coding = utf-8 -*-
# @time:2023/9/3 11:22
# Author:lizhuang
# @File:mdbb数据.py
# @Software:PyCharm
import pandas as pd
import pyodbc
import pandas as pd
import sqlite3
import re


def 读取数据库(数据库文件=r'../gearbox/GearDatabase.db', 表名称='调心球轴承'):
    # Validate the table name to prevent SQL injection

    conn = sqlite3.connect(数据库文件)

    try:
        # Construct the SQL query
        sql = f"SELECT * FROM {表名称}"

        # Read the data into a pandas DataFrame
        df = pd.read_sql_query(sql, conn)

        # Perform data cleaning operations
        df = df.dropna(how='all')
        df = df.fillna(' ')

        # Print the DataFrame (optional, remove or comment out for production use)
        print(df)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the database connection
        conn.close()

    return df


def 查询值(带型,行,列):
    mdb_file = './GearDatabase.mdb'
    driver = '{Microsoft Access Driver (*.mdb, *.accdb)}'
    conn = pyodbc.connect(f'Driver={driver};DBQ={mdb_file}')
    cur = conn.cursor()
    '''for table_name in cur.tables(tableType='TABLE'):
        print(table_name.table_name)
    # 执行sql
    sql = 'select * from V带工况系数KA'
    cur.execute(sql)
    # row = cur.fetchone()
    rows = cur.fetchall()'''
    name = str(带型)
    sql = "SELECT * FROM " + str(name)
    # sql = 'SELECT * FROM V带工况系数KA'
    df = pd.read_sql(sql, conn)
    df = df.dropna(how='all')
    df = df.fillna(' ')
    print(df)
    cur.close()
    conn.close()
    return
if __name__ == '__main__':
    读取数据库(表名称='V带工况系数KA')