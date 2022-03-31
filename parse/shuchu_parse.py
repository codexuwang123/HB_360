#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:shuchu_parse.py
# 创建日期:2022/3/19 9:23
# 作者:XU
# 联系邮箱:iswongx@163.com


import re

# 书橱网站解析
def shuchu_par(data, dict,dict_details):

    author = re.findall('<ul class="list">.*?<span>.*?作者：.*?<a.*?>(.*?)</a>.*?</span>', data, re.S)
    if author:
        dict_details['author'] = author[0].strip()
    else:
        dict_details['author'] = ''
    description = re.findall('<div class="intro_txt">(.*?)</div>', data, re.S)
    if description:
        dict_details['describe'] = description[0].replace('<em class="black9">', '').replace('</em><p>', '').replace(
            '</p><p>', '').replace('</p>', '').replace('\r\n', '').strip()
    else:
        dict_details['describe'] = ''
    dict_details['protagonist'] = ''
    dict_details['tittle'] = ''
    dict['details'] = dict_details
