#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:laishu8.py
# 创建日期:2022/3/15 9:35
# 作者:XU
# 联系邮箱:iswongx@163.com

import re


# 来书吧中文网
def lais(data, dict,dict_details):

    author = ''
    author1 = re.findall('<div id="maininfo">.*?<h3>作者：<a.*?>(.*?)</a></h3>', data, re.S)
    if author1:
        author = author1[0]
        dict_details['author'] = author
    else:
        dict_details['author'] = author
    description = ''
    description1 = re.findall('<div id="intro">.*?<p>(.*?)</p>.*?</div>', data, re.S)
    if description1:
        description = description1[0]
        dict_details['describe'] = description
    else:
        dict_details['describe'] = description
    dict_details['tittle'] = ''
    dict['details'] = dict_details
    return dict
