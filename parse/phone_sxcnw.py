#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:phone_sxcnw.py
# 创建日期:2022/3/22 11:42
# 作者:XU
# 联系邮箱:iswongx@163.com

import re

#解析手机端书香电子
def phone_sxcnw(data,dict):
    dict_details = {}

    author = re.findall('<div class="jie">.*?<br>.*?<span>(.*?)</span>.*?<br>', data, re.S)
    if author:
        dict_details['author'] = author[0].replace('作者','').strip().replace('/','')
    else:
        dict_details['author'] = ''
    description = re.findall('<div class="bookinfo">(.*?)</div>', data, re.S)
    if description:
        dict_details['describe'] = description[0].strip()
    else:
        dict_details['describe'] = ''
    dict_details['protagonist'] = ''
    tittle = re.findall('<div class="jie">.*?<h1>(.*?)</h1>',data,re.S)
    if tittle:
        dict_details['tittle'] = tittle[0].strip()
    else:
        dict_details['tittle'] = ''
    dict['details'] = dict_details