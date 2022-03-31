#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:ysg_parse.py
# 创建日期:2022/3/13 12:16
# 作者:XU
# 联系邮箱:iswongx@163.com


import re


# 阅书阁小说解析
def parse_ysg(data, dict,dict_details):

    author = re.findall('<div id="info">.*?<p>作.*?者：(.*?)</p>', data, re.S)
    if author:
        dict_details['author'] = author[0]
    else:
        dict_details['author'] = ''
    description = re.findall('<div id="intro">.*?<p>(.*?)</p>', data, re.S)
    if description:
        dict_details['describe'] = description[0]
    else:
        dict_details['describe'] = ''
    dict_details['protagonist'] = ''
    dict_details['tittle'] = ''

    dict['details'] = dict_details
    # print(dict, '阅书阁 进来了===========================')
