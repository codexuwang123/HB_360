#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:redis_connect.py
# 创建日期:2022/3/17 9:57
# 作者:XU
# 联系邮箱:iswongx@163.com

import redis
from settings import test_redis

# 连接redis基本配置
class Redis_connect():

    def __init__(self):

        # redis 链接池
        conn_pool = redis.ConnectionPool(host=test_redis['host'], password=test_redis['password'], port=test_redis['port'], db=test_redis['db'])
        self.job_redis = redis.Redis(connection_pool=conn_pool)

    def search_data_redis(self, redis_key):
        # 查询redis 数据
        return self.job_redis.spop(redis_key)

    def insert_data_redis(self, redis_key, values):
        # redis 批量插入数据
        return self.job_redis.sadd(redis_key, values)

    def search_all_data(self, redis_key):
        # redis 查询所有数据
        return self.job_redis.smembers(redis_key)

    def delete_redis_all(self,redis_key):
        # redis 删除指定key 下的所有数据
        return self.job_redis.delete(redis_key)
