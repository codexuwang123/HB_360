#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:soxscc_parse.py
# 创建日期:2022/3/22 14:03
# 作者:XU
# 联系邮箱:iswongx@163.com

import re


# 解析搜小说
def soxscc_par(data, dict,dict_details):

    if '作者' in data:
        author = re.findall('\（作者：(.*?)\）', data, re.S)
        if author:
            dict_details['author'] = author[0].strip().replace('&gt;', '')
        else:
            dict_details['author'] = ''
    description = re.findall('<div class="txt_description">.*?<p>(.*?)</p>', data, re.S)
    if description:
        dict_details['describe'] = description[0].strip()
    else:
        dict_details['describe'] = ''
    dict_details['protagonist'] = ''
    dict_details['tittle'] = ''

    dict['details'] = dict_details
