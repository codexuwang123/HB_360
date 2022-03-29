#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:rpg66_parse.py
# 创建日期:2022/3/18 22:49
# 作者:XU
# 联系邮箱:iswongx@163.com


#解析橙光

import re

def chenguang_par(data,dict):
    dict_details = {}
    author = re.findall('<div id="info">.*?<p>作.*?者：(.*?)</p>', data, re.S)
    if author:
        dict_details['author'] = author[0]
    else:
        dict_details['author'] = ''
    description = re.findall('<meta name="description".*?content="(.*?)"', data, re.S)
    if description:
        dict_details['describe'] = description[0].strip()
    else:
        dict_details['describe'] = ''
    dict_details['protagonist'] = ''
    dict_details['tittle'] = ''
    dict['details'] = dict_details