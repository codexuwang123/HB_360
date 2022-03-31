#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:save_data_to_sql.py
# 作者:XU
# 联系邮箱:iswongx@163.com


import pymysql
from settings import test_sql


# 数据数据存储
class Save_score_to_sql(object):

    # 初始化数据库参数
    def __init__(self):
        self.host = test_sql['host']
        self.user = test_sql['user']
        self.password = test_sql['password']
        self.db = test_sql['db']
        self.conn = pymysql.connect(host=self.host, user=self.user, passwd=self.password, db=self.db,
                                    cursorclass=pymysql.cursors.DictCursor, charset='utf8mb4')
        self.cur = self.conn.cursor()

    # 首页数据库数据插入
    def search_data_to_sql(self, data):
        # print(data, '======================')
        sql = 'insert into search_data(id,number,tittle,key_word,skip_url,true_url)VALUES (0,"{}","{}","{}","{}","{}")'.format(
            data['number'], data['tittle'], data['keyword'], data['url'], data['true_url'])
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            # 插入数据发生错误回滚
            self.conn.rollback()
            print(e, sql, '===============')

    # # 详情页数据库插入
    # def details_data_to_sql(self, data):
    #     print(data, '详情页======================')
    #     sql = 'insert into details_data(id,number,author,tittle,description,protagonist)VALUES (0,"{}","{}","{}","{}","{}")'.format(
    #         data['number'], data.get('details').get('author', ''), data.get('details').get('tittle', ''),
    #         data.get('details').get('describe', ''), data.get('details').get('protagonist', ''))
    #     # print(sql,'详情页=========')
    #     try:
    #         self.cur.execute(sql)
    #         self.conn.commit()
    #     except Exception as e:
    #         # 插入数据发生错误回滚
    #         self.conn.rollback()
    #         print(e, sql, '==================')

    # 详情页数据库插入
    def details_data_to_sql(self, data):
        print(data, '详情页======================')
        sql = 'insert into details_data(id,number,author,author_score,book_name_score,section_score,weight,tittle,description,protagonist)VALUES (0,"{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(
            data['number'], data.get('details').get('author', ''), data.get('details').get('author_score'),
            data.get('details').get('book_name_score'), data.get('details').get('section_score'),
            data.get('details').get('weight'), data.get('details').get('tittle', ''),
            data.get('details').get('describe', ''), data.get('details').get('protagonist', ''))
        # print(sql,'详情页=========')
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            # 插入数据发生错误回滚
            self.conn.rollback()
            print(e, sql, '==================')

    # 整页面数据库插入
    def book_html_to_sql(self, data):
        # print(data, '整页数据插入======================')
        sql = 'insert into book_data(id,number,book_name,true_url,book_detail)VALUES (0,"{}","{}","{}","{}")'.format(
            data['number'], data['book_name'], data['true_url'], data['book_detail'])
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            # 插入数据发生错误回滚
            self.conn.rollback()
            print(e, sql, '==================')


    # 关键词查询
    def get_keyword(self):

        sql = 'select search_keyword,spider_status,section_name,author from basic_information where spider_status=0 and channel_name=2'
        try:
            self.cur.execute(sql)
            results = self.cur.fetchall()
            return results
        except Exception as e:
            print(e, sql, '关键词数据可查询操作===')

    # 更改状态
    def undate_data(self, status_, keyword):
        # 更改爬虫配置表状态
        sql = "UPDATE basic_information SET spider_status = '{}' WHERE search_keyword = '{}' and  channel_name=2".format(
            status_, keyword)
        try:
            # print(sql)
            # 执行SQL语句
            self.cur.execute(sql)
            # 提交到数据库执行
            self.conn.commit()
        except Exception as e:
            print(e, '数据更新时候出现异常===')
            # 发生错误时回滚
            self.conn.rollback()

    # 关闭数据库
    def close(self):
        self.cur.close()
        self.conn.close()
