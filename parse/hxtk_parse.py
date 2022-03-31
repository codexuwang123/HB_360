#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:hxtk_parse.py
# 创建日期:2022/3/21 10:45
# 作者:XU
# 联系邮箱:iswongx@163.com


import re

# 华夏天空小说网
def hxtk_par(data,dict,dict_details):

    author = re.findall('class="writer-name">(.*?)</a>', data, re.S)
    if author:
        dict_details['author'] = author[0].strip()
    else:
        dict_details['author'] = ''
    description = re.findall('<span class="part isShow">(.*?)</span>', data, re.S)
    if description:
        dict_details['describe'] = description[0].strip().replace('&nbsp;','')
    else:
        dict_details['describe'] = ''
    dict_details['protagonist'] = ''
    tittle = ''
    tittle1 = re.findall('<div class="book-name">.*?<h1>(.*?)</h1>',data,re.S)
    if tittle1:
        dict_details['tittle'] = tittle1[0].strip()
    else:
        dict_details['tittle'] = tittle

    dict['details'] = dict_details