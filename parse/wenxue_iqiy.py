#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:wenxue_iqiy.py
# 创建日期:2022/3/22 9:54
# 作者:XU
# 联系邮箱:iswongx@163.com


import re


# 文学爱奇艺
def iqiy(data, dict,dict_details):

    author = re.findall('<em class="writerName">(.*?)</em>', data, re.S)
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

    tittle1 = re.findall('<strong class="reader-chapter-tit">(.*?)</strong>',data,re.S)
    tittle = ''
    if tittle1:
        dict_details['tittle'] = tittle1[0].strip()
    else:
        dict_details['tittle'] = tittle

    dict['details'] = dict_details
