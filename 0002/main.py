#!/usr/bin/python
# _*_ coding: utf-8 _*_

# 第0002题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中

__author__ = 'Insomnia'

import random, string, pymysql

# 打开数据库连接
db = pymysql.connect('172.17.0.3', 'root', 'root', 'test')

def rand_str(num, length = 7):
    print('Begin!')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    chars = string.ascii_letters + string.digits  #所有字母和数字
    codes = []
    for i in range(num):
        code = ''  # 激活码/优惠券
        for j in range(length):
            code += random.choice(chars)
        codes.append('("' + code + '")')

    # sql批量插入语句
    codes_str = ','.join(codes)
    sql = "INSERT INTO test(code) VALUES %s" % codes_str
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    print('End!')

if __name__ == '__main__':
    rand_str(200)

# 关闭数据库连接
db.close()