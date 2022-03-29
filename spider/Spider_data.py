#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:Spider_data.py
# 创建日期:2022/3/10 10:23
# 作者:XU
# 联系邮箱:iswongx@163.com
import time

import requests
import re
from parse import format_base_spdb
import random
from to_sql import save_data_to_sql
import json
list = []

from redis_client import redis_connect
from settings import set_
from settings import ua
conn = redis_connect.Redis_connect()

# 主要爬虫方法
class Spider_desc_360():

    # 基本请求头配置
    def __init__(self, wd):
        self.uA = ua.get('user_agent')
        self.wd = wd
        # logging_.info('搜索引擎360，正在爬取={}相关内容。'.format(self.wd))

    # 解析主函数
    def spider_360(self, pn, keyword=None,list_redis=None):

        self.url = 'https://www.so.com/s?'
        self.params = {
            'q': keyword,
            'pn': pn,
            'src': 'srp_paging',
            'fr': 'none'
        }
        self.headers = {
            'User-Agent': random.choice(self.uA),
            'X-Requested-With': 'XMLHttpRequest'
        }
        res = requests.get(self.url, headers=self.headers, params=self.params, verify=False)
        if res.status_code == 200:
            # print(res.text)
            data = re.findall('<h3.*?class="res-title.*?<a.*?href="(.*?)".*?<em>(.*?)</a>', res.text, re.S)
            print(data, len(data))
            format_base_spdb.format_text(first_data=data, keyword=keyword,list_redis=list_redis)
        else:
            print(res.text)


# 主函数调用
def last_mains():
    s_data = save_data_to_sql.Save_score_to_sql()
    # 数据库获取关键次列表
    keyword_list = s_data.get_keyword()
    if keyword_list:
        for i in keyword_list:
            list_redis = []
            dict_redis = {}
            dict_redis['book_name'] = i.get('Search_Keyword')
            print(dict_redis)
            for n in range(1, set_.get('max_page')):
                spider_self = Spider_desc_360(wd=i.get('Search_Keyword'))
                spider_self.spider_360(pn=n, keyword=spider_self.wd,list_redis=list_redis)
            dict_redis['data'] = list_redis
            dict_ = json.dumps(dict_redis, ensure_ascii=False)
            print(dict_)
            conn.insert_data_redis(redis_key='360s', values=dict_)
            print('redis 数据存放成功')
            # 更新爬虫状态
            s_data.undate_data(status_='1', keyword=i.get('Search_Keyword'))
        # 关闭数据库连接
        # s_data.close()
    else:
        print('========温馨提示：没有有效关键词需要爬取=======')


if __name__ == '__main__':

    while True:
        time.sleep(3)
        last_mains()

