#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:qbxsw_parse.py
# 创建日期:2022/3/13 14:11
# 作者:XU
# 联系邮箱:iswongx@163.com


import re

# 全本小说网解析
def qbxsw_parse(data,dict,dict_details):

    author = ''
    author1 = re.findall('<span class="author">(.*?)</span></p>', data, re.S)
    if author1:
        author = author1[0]
        dict_details['author'] = author
    else:
        dict_details['author'] = author
    description =''
    description1 = re.findall('<div class="description">(.*?)</div>',data,re.S)
    if description1:
        description = description1[0]
        dict_details['describe'] = description
    else:
        dict_details['describe'] = description
    dict_details['tittle'] = ''
    dict['details'] = dict_details