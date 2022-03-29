#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:xuanshu_parse.py
# 创建日期:2022/3/12 11:53
# 作者:XU
# 联系邮箱:iswongx@163.com


import re

# 选书网
def quanshu(data,dict):
    dict_details = {}
    author = re.findall('<div class="info_des">.*?<dl>作.*?者：(.*?)</dl>', data, re.S)
    if author:
        dict_details['author'] = author[0]
    else:
        dict_details['author'] = ''
    description = re.findall('<div id="down"></div>(.*?)</div>', data, re.S)
    if description:
        dict_details['describe'] = description[0].strip()
    else:
        dict_details['describe'] = ''
    dict_details['protagonist'] = ''
    dict_details['tittle'] = ''

    dict['details'] = dict_details