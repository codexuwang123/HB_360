#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:sxcnw_parse.py
# 创建日期:2022/3/22 10:19
# 作者:XU
# 联系邮箱:iswongx@163.com

import re


# 书香电子书
def sxdz_par(data, dict):
    dict_details = {}
    author = re.findall('<div class="book-title clear">.*?<span>(.*?)</span>', data, re.S)
    if author:
        dict_details['author'] = author[0].replace('[全集完本]','').replace('&nbsp;','').strip()
    else:
        dict_details['author'] = ''
    description = re.findall('<div id="intro">.*?<p>(.*?)</p>', data, re.S)
    if description:
        dict_details['describe'] = description[0]
    else:
        dict_details['describe'] = ''
    dict_details['protagonist'] = ''

    tittle = re.findall('<div class="book-title clear">.*?<h1>(.*?)</h1>', data, re.S)
    if tittle:
        dict_details['tittle'] = tittle[0].strip()
    else:
        dict_details['tittle'] =''
    dict['details'] = dict_details
