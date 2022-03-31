#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:parse_baidu.py
# 创建日期:2022/3/12 17:28
# 作者:XU
# 联系邮箱:iswongx@163.com
import json
import re

import requests


# 解析百度小说代码
def parse_b(url, dict,dict_details):
    num = re.findall('gid=(\d+)', url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    dict1 = {}
    dict1["book_id"] = str(num[0])
    dict_ = json.dumps(dict1)
    new_url = 'https://dushu.baidu.com/api/pc/getDetail?data={}'.format(dict_)
    res = requests.get(url=new_url, headers=headers)
    if res.status_code == 200:
        data = res.json()
        new_data = data.get('data').get('novel')
        dict_details['tittle'] = new_data.get('title','')
        dict_details['author'] = new_data.get('author','')
        dict_details['describe'] = new_data.get('description','')
        dict['details'] = dict_details
        # print(dict, '百度0999991')
