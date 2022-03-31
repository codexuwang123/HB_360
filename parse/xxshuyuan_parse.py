#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:xxshuyuan_parse.py
# 创建日期:2022/3/22 10:31
# 作者:XU
# 联系邮箱:iswongx@163.com

import re


# 潇湘书院
def xxshuyuan_par(data, dict,dict_details):

    author = re.findall('<div class="title">.*?<span>(.*?)</span>.*?</div>', data, re.S)
    if author:
        dict_details['author'] = author[0].replace('文&nbsp;', '').replace('/&nbsp;', '').replace('\r\n','').strip()
    else:
        dict_details['author'] = ''
    description = re.findall('<div id="intro">.*?<p>(.*?)</p>', data, re.S)
    if description:
        dict_details['describe'] = description[0]
    else:
        dict_details['describe'] = ''
    dict_details['protagonist'] = ''
    tittle = re.findall('<div class="title">.*?<h1>(.*?)</h1>.*?</div>', data, re.S)
    if tittle:
        dict_details['tittle'] = tittle[0]
    else:
        dict_details['tittle'] = ''
    dict['details'] = dict_details
