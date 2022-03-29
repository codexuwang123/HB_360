#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:luochen_parse.py
# 创建日期:2022/3/18 16:10
# 作者:XU
# 联系邮箱:iswongx@163.com

import re


# 阅书阁小说解析
def parse_ysg(data, dict):
    dict_details = {}
    author = re.findall('<i class="iconfont icon-biaoqian-zuozhe1">.*?<p.*?>(.*?)</p>', data, re.S)
    if author:
        dict_details['author'] = author[0]
    else:
        dict_details['author'] = ''
    description = re.findall('<p class="book-introduce-container">(.*?)<p class="open-close">', data, re.S)
    description1 = ''
    if description:
        dict_details['describe'] = description[0].strip().replace('&nbsp;', '')
    else:
        dict_details['describe'] = description1
    dict_details['protagonist'] = ''
    tittle = ''
    tittle1 = re.findall('<span class="booktitle">(.*?)</span>', data)
    if tittle1:
        dict_details['tittle'] = tittle1[0].strip()
    else:
        dict_details['tittle'] = tittle

    dict['details'] = dict_details
    # print(dict, '阅书阁 进来了===========================')
