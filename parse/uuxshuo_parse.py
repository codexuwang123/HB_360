#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:uuxshuo_parse.py
# 创建日期:2022/3/16 15:03
# 作者:XU
# 联系邮箱:iswongx@163.com


import re

# uu小说网数据解析
def uuxs_par(data,dict,dict_details):

    author = re.findall('<p class="author">作者：<span class="black"><a.*?>(.*?)</a>', data, re.S)
    if author:
        dict_details['author'] = author[0].strip()
    else:
        dict_details['author'] = ''
    description = re.findall('<div class="r_cons">(.*?)</div>', data, re.S)
    if description:
        dict_details['describe'] = description[0].strip()
    else:
        dict_details['describe'] = ''
    dict_details['protagonist'] = ''
    dict_details['tittle'] = ''
    dict['details'] = dict_details
