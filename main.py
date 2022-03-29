#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:settings.py
# 创建日期:2022/3/10 10:19
# 作者:XU
# 联系邮箱:iswongx@163.com

import time
from to_sql import save_data_to_sql
from parse import format_base_spdb
from concurrent.futures import ThreadPoolExecutor
import uuid
import json
from redis_client import redis_connect
from settings import set_

# 实例化sql链接
s_data = save_data_to_sql.Save_score_to_sql()


#总调用

def main_parse(dict):
    # print(i, '--------')
    print('线程进来了================')
    print(dict,'==========---')
    new_tittle = dict.get('tittle')
    new_url = dict.get('url')
    true_url12 = format_base_spdb.get_360_rue_url(skip_url=new_url)
    details_data, true_url = format_base_spdb.get_true(url=true_url12)
    dict['true_url'] = true_url12
    new_keyword = dict.get('keyword')
    number = str(uuid.uuid1()).replace('-', '')
    dict['number'] = number
    format_base_spdb.get_(new_keyword=new_keyword, new_tittle=new_tittle, details_data=details_data, true_url=true_url,dict=dict)


if __name__ == '__main__':

    while True:
        conn = redis_connect.Redis_connect()
        flag_data = conn.search_all_data(redis_key='360s')
        print(flag_data,'''==============11111111111111''')
        time.sleep(3)
        print('等待新任务中========')
        try:
            flags = len(flag_data)
            if flags == 0:
                continue
            else:
                dta = conn.search_data_redis(redis_key='360s')
                dict = json.loads(dta)
                book_name = dict.get('book_name')
                data_book = dict.get('data')
                # 最大任务数
                with ThreadPoolExecutor(max_workers=set_.get('max_workers'))as f:
                    results = f.map(main_parse, data_book)
                s_data.undate_data(status_='2', keyword=book_name)
        except Exception as e:
            print(e, '=============')





