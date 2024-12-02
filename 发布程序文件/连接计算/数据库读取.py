# -*- coding = utf-8 -*-
# @time:2023/12/21 19:20
# Author:lizhuang
# @File:数据库读取.py
# @Software:PyCharm
import pandas as pd
import sqlite3


def read_table_to_dataframe(database_file, table_name):
    # 连接到数据库
    conn = sqlite3.connect(database_file)

    # 读取数据库中的数据表到 DataFrame
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, conn)

    # 关闭数据库连接
    conn.close()

    return df

import sqlite3

# 连接到 SQLite 数据库
def connect_to_database(db_file):
    connection = sqlite3.connect(db_file)
    return connection


# 读取数据库表中的某一行
def read_specific_row(connection, table_name, condition_column, condition_value):
    cursor = connection.cursor()
    query = f"SELECT * FROM {table_name} WHERE {condition_column} = ?"
    cursor.execute(query, (condition_value,))
    selected_row = cursor.fetchone()
    return selected_row


# 添加一行数据到数据库表
def add_row(connection, table_name, data):
    cursor = connection.cursor()
    columns = ', '.join(data.keys())
    placeholders = ', '.join('?' * len(data))
    values = tuple(data.values())
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    cursor.execute(query, values)
    connection.commit()


# 更新数据库表中的某一行数据
def update_row(connection, table_name, update_data, condition_column, condition_value):
    cursor = connection.cursor()
    set_clause = ', '.join([f"{key} = ?" for key in update_data.keys()])
    values = tuple(update_data.values())
    query = f"UPDATE {table_name} SET {set_clause} WHERE {condition_column} = ?"
    values += (condition_value,)
    cursor.execute(query, values)
    connection.commit()


if __name__ == "__main__":
    '''db_file = 'your_database.db'  # 替换为你的数据库文件路径
    table_name = 'your_table'  # 替换为你的表名

    # 连接到数据库
    connection = connect_to_database(db_file)

    # 读取特定行示例
    condition_column = 'column_name'  # 替换为条件列名
    condition_value = 'condition_value'  # 替换为条件值
    row = read_specific_row(connection, table_name, condition_column, condition_value)
    print("Selected row:", row)

    # 添加一行数据示例
    new_data = {'column1': 'value1', 'column2': 'value2'}  # 替换为要添加的数据
    add_row(connection, table_name, new_data)
    print("New row added.")

    # 更新一行数据示例
    update_data = {'column1': 'new_value1', 'column2': 'new_value2'}  # 替换为要更新的数据
    update_condition_column = 'column_name'  # 替换为更新条件列名
    update_condition_value = 'condition_value'  # 替换为更新条件值
    update_row(connection, table_name, update_data, update_condition_column, update_condition_value)
    print("Row updated.")

    # 关闭数据库连接
    connection.close()'''

    # 使用函数读取指定表格
    result_df = read_table_to_dataframe('../连接计算/luosuanshuju.db', '刚度')

    # 打印 DataFrame 的前几行数据
    print(result_df.head())