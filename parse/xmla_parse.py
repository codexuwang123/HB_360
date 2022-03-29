#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:xmla_parse.py
# 创建日期:2022/3/12 17:48
# 作者:XU
# 联系邮箱:iswongx@163.com

import re
import json


# 喜马拉雅简介内容解析

def parse_xmly_desc(string):
    xc = re.sub(r'style=\\font-size:\d+px;', '', string)
    xc = re.sub(r'margin:\d+px 0px;', '', xc)
    xc = re.sub(r'color:rgb\(\d+, \d+, \d+\);', '', xc)
    xc = re.sub(r'border-left:\d+px solid rgb\(\d+, \d+, \d+\);', '', xc)
    xc = re.sub(r'padding-left:\d+px;', '', xc)
    xc = re.sub(r'\\\\u\d+e\\u\d+cp style=\\color:#\d+;', '', xc)
    xc = re.sub(r'font-size:\d+px;', '', xc)
    xc = re.sub(r'data-flag=\\bk-span\\\\u\d+e', '', xc)
    xc = re.sub(r'style=\\color:#\d+;', '', xc)
    xc = re.sub(r'font-weight:normal;', '', xc)
    xc = re.sub(r'line-height:\d+px;', '', xc)
    xc = xc.replace(r'\u003c/p', '')
    xc = xc.replace(r'\u003e', '')
    xc = xc.replace(r'\u003cp', '')
    xc = xc.replace(r'\u003c/', '')
    xc = xc.replace(r'font-family:Helvetica,', '')
    xc = xc.replace(r'hyphens:auto;', '')
    xc = xc.replace(r'text-align:justify;', '')
    xc = xc.replace(r'sans-serif;', '')
    xc = xc.replace('color:#333333;', '')
    xc = xc.replace('data-flag=\\normal\\', '')
    xc = xc.replace('Arial,', '')
    xc = xc.replace('style=\\display:none\\', '')
    xc = xc.replace('data-preview=\\true\\span', '')
    xc = re.sub(r'style=\\color:#\d+E\d+;', '', xc)
    strings = xc.replace('text-decoration:none;', '')
    strings = strings.replace('style=\\"', '')
    strings = strings.replace('data-flag=\\"', '')
    strings = strings.replace('normal\\"', '')
    strings = strings.replace('style=\\"', '')
    strings = strings.replace(r'\u003cspan', '')
    strings = strings.replace(r'\u003cbr', '')
    strings = strings.replace(r'/span', '')
    strings = strings.replace(r'\"', '').strip()
    strings = strings.replace(r'display:none', '').strip()
    strings = strings.replace(r'data-preview=truespan"', '').strip()
    if '内容介绍' in strings:
        x = xc[xc.find('内容介绍')::]
        x = x.replace(r'\u003cb', '')
        x = x.replace('<span', '')
        x = x.replace('\\', '')
        # print(x)
        return x
    elif '内容简介' in strings:
        x = xc[xc.find('内容介绍')::]
        x = x.replace(r'\u003cb', '')
        x = x.replace('<span', '')
        x = x.replace('\\', '')
        # print(x)
        return x
    else:
        return strings


# 喜马拉雅解析
def smly_(data, dict):
    dict_details = {}
    new_data = re.findall(r'"tdkMeta":(.*?\})\}', data)
    description = re.findall('"richIntro":"(.*?)"shortIntro"', data, re.S)
    if description:
        xcd = parse_xmly_desc(string=description[0])
        dict_details['describe'] = xcd
    else:
        dict_details['describe'] = ''
    if new_data:
        new_xmly = new_data[0]
        new_xmly_ = json.loads(new_xmly)
        dict_details['tittle'] = new_xmly_.get('title')
    dict['details'] = dict_details
    return dict
