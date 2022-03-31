#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:mq_parse.py
# 创建日期:2022/3/13 14:34
# 作者:XU
# 联系邮箱:iswongx@163.com


import re

#魔情
def mq_par(data,dict,dict_details):

    author = ''
    author1 = re.findall('<meta name="author" content=".*?作者：{0,1}"(.*?)".*?>', data, re.S)
    if author1:
        author = author1[0]
        dict_details['author'] = author
    else:
        dict_details['author'] = author
    description = ''
    description1 = re.findall('<p id="summary">(.*?)</p>',data,re.S)
    if description1:
        description = description1[0]
        dict_details['describe'] = description
    else:
        dict_details['describe'] = description
    dict_details['tittle'] = ''
    dict['details'] = dict_details
    return dict
