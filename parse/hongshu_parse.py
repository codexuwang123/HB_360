#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:hongshu_parse.py
# 创建日期:2022/3/22 17:09
# 作者:XU
# 联系邮箱:iswongx@163.com

import re

#红薯网
def hongshu_par(data,dict):
    dict_details = {}
    author = re.findall('<p class="top20">.*?作者：<a.*?>(.*?)</a>.*?</p>', data, re.S)
    if author:
        dict_details['author'] = author[0].strip()
    else:
        dict_details['author'] = ''
    description = re.findall('<div id="intro">.*?<p>(.*?)</p>', data, re.S)
    if description:
        dict_details['describe'] = description[0]
    else:
        dict_details['describe'] = ''
    dict_details['protagonist'] = ''
    tittle = re.findall(' <div class="chapter01 lf15 clearfix">.*?<h1>.*?<a class="qh".*?>(.*?)</a>.*?</h1>',data,re.S)
    if tittle:
        dict_details['tittle'] = tittle[0].strip()
    else:
        dict_details['tittle'] = ''

    dict['details'] = dict_details
