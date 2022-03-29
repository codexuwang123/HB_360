#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:yuedyue_parse.py
# 创建日期:2022/3/22 17:01
# 作者:XU
# 联系邮箱:iswongx@163.com

import re


# 阅读悦小说解析
def yuedyue_par(data, dict):
    dict_details = {}
    author = re.findall('<div class="block_txt2">.*?作者：<a href="/author.*?">(.*?)</a></p>', data, re.S)
    if author:
        dict_details['author'] = author[0].strip()
    else:
        dict_details['author'] = ''
    description = re.findall('<div class="intro_info">(.*?)</div>', data, re.S)
    if description:
        dict_details['describe'] = description[0].strip()
    else:
        dict_details['describe'] = ''
    dict_details['protagonist'] = ''
    tittle = re.findall('<div class="block_txt2">.*?<p><a ><h2>(.*?)</h2></a></p>', data, re.S)
    if tittle:
        dict_details['tittle'] = tittle[0]
    else:
        dict_details['tittle'] = ''

    dict['details'] = dict_details
