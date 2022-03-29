#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:yjgmmc_par.py
# 创建日期:2022/3/22 13:43
# 作者:XU
# 联系邮箱:iswongx@163.com

import re


# 二月天小说解析
def eryuet_par(data, dict):
    dict_details = {}
    author = re.findall('<div class="title-info">.*?<a href=".*?">(.*?)</a>', data, re.S)
    if author:
        dict_details['author'] = author[0]
    else:
        dict_details['author'] = ''
    description = re.findall('<p class="info-text f-big">(.*?)</p>', data, re.S)
    if description:
        dict_details['describe'] = description[0].strip().replace('&nbsp;','')
    else:
        dict_details['describe'] = ''
    dict_details['protagonist'] = ''
    tittle = re.findall('<div class="title-info">.*?<h4>(.*?)</h4>',data,re.S)
    if tittle:
        dict_details['tittle'] = tittle[0].strip()
    else:
        dict_details['tittle'] = ''

    dict['details'] = dict_details
