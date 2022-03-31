#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:soxs_parse.py
# 创建日期:2022/3/15 11:21
# 作者:XU
# 联系邮箱:iswongx@163.com

import re


# 搜小说详情解析
def soxs_par(data, dict,dict_details):

    author = re.findall('<div class="pods">.*?<a .*?>(.*?)</a>.*?</div>', data, re.S)
    if author:
        dict_details['author'] = author[0]
    else:
        dict_details['author'] = ''
    description = re.findall('<div class="txt_description">.*?<p>(.*?)</p>', data, re.S)
    if description:
        dict_details['describe'] = description[0]
    else:
        dict_details['describe'] = ''
    dict_details['protagonist'] = ''
    tittle = ''
    tittle1 = re.findall('<h1 class="title">(.*?)</h1>', data, re.S)
    if tittle1:
        dict_details['tittle'] = tittle1[0]
    else:
        dict_details['tittle'] = tittle

    dict['details'] = dict_details
    # print(dict, '蜻蜓 进来了===========================')
