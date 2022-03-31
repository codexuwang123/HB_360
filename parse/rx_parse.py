#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:rx_parse.py
# 创建日期:2022/3/13 14:56
# 作者:XU
# 联系邮箱:iswongx@163.com


import re

#若夏
def rx_par(data,dict,dict_details):


    author = ''
    if '作者' in data:
        author1 = re.findall('作者：(.*?)</a>', data, re.S)
        if author1:
            xc = re.sub(r'<[^>]+>','',author1[0].strip())
            dict_details['author'] = xc.strip()
        else:
            dict_details['author'] = author
    description = ''
    description1 = re.findall('"description":(.*?)"pubDate"',data,re.S)
    if description1:
        description = description1[0]
        dict_details['describe'] = description.replace('&ldquo;','')
    else:
        dict_details['describe'] = ''
    dict_details['tittle'] = ''
    dict['details'] = dict_details
    return dict