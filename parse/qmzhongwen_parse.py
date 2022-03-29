#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:qmzhongwen_parse.py
# 创建日期:2022/3/15 16:07
# 作者:XU
# 联系邮箱:iswongx@163.com

import requests
import re

headers1 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }





def get_script_data(base_url):
    '''
    获取js相应参数
    '''

    response = requests.get(base_url, headers=headers1)
    arg1 = re.search("arg1='([^']+)'", response.text).group(1)
    return arg1

def hexXor(_0x4e08d8, _0x23a392):
    '''
    对数据进行hexXor处理
    '''

    _0x5a5d3b = ''
    _0xe89588 = 0x0
    while _0xe89588 < len(_0x23a392) and _0xe89588 < len(_0x4e08d8):
        _0x401af1 = int(_0x23a392[_0xe89588: _0xe89588 + 0x2], 16)
        _0x105f59 = int(_0x4e08d8[_0xe89588: _0xe89588 + 0x2], 16)
        _0x189e2c = hex(_0x401af1 ^ _0x105f59)
        if len(_0x189e2c) == 0x1:
            _0x189e2c = '\x30' + _0x189e2c
        _0x5a5d3b += _0x189e2c[2:]

        _0xe89588 += 0x2
    return _0x5a5d3b

def unsbox(arg):
    _0x4b082b = [0xf, 0x23, 0x1d, 0x18, 0x21, 0x10, 0x1, 0x26, 0xa, 0x9, 0x13, 0x1f, 0x28, 0x1b, 0x16, 0x17, 0x19,
                 0xd,
                 0x6, 0xb, 0x27, 0x12, 0x14, 0x8, 0xe, 0x15, 0x20, 0x1a, 0x2, 0x1e, 0x7, 0x4, 0x11, 0x5, 0x3, 0x1c,
                 0x22, 0x25, 0xc, 0x24]
    _0x4da0dc = [''] * 40
    _0x12605e = ''
    for _0x20a7bf in range(0, len(arg)):
        _0x385ee3 = arg[_0x20a7bf]
        for _0x217721 in range(0, len(_0x4b082b)):
            if _0x4b082b[_0x217721] == _0x20a7bf + 0x1:
                _0x4da0dc[_0x217721] = _0x385ee3
    _0x12605e = ''.join(_0x4da0dc)
    return _0x12605e



#七猫数据解析
def qimao_parse(data,dict):

    dict_details = {}
    author = re.findall('<p class="p-name"><em>作者：</em><a.*?>(.*?)</a>',data,re.S)
    if author:
        dict_details['author'] = author[0].replace('&nbsp;',' ').strip()
    else:
        dict_details['author'] = ''
    description = re.findall(' <div class="article">(.*?)</div>', data, re.S)
    if description:
        dict_details['describe'] = description[0].replace('\n','').strip()
    else:
        dict_details['describe'] = ''
    #主角
    protagonist = ''
    protagonist1 = re.findall('<em>主角：</em>(.*?)</p>',data,re.S)
    if protagonist1:
        dict_details['protagonist'] = protagonist1[0]
    else:
        dict_details['protagonist'] = protagonist
    tittle = ''
    tittle1 = re.findall('<h1 class="title">(.*?)</h1>', data, re.S)
    if tittle1:
        dict_details['tittle'] = tittle1[0]
    else:
        dict_details['tittle'] = tittle

    dict['details'] = dict_details
    # print(dict, '七猫 进来了===========================')

# 七猫中文网
def get_acw_sc_v2(base_url):

    # 七猫中文网会有set_cookies加密，会不停检测cookies acw_sc__v2 的cookies值
    # 从而限制访问页面
    # base_url = 'https://www.qimao.com/shuku/205854/'
    arg1 = get_script_data(base_url)
    key = '3000176000856006061501533003690027800375'
    _0x23a392 = unsbox(arg1)
    arg2 = 'acw_sc__v2=' + hexXor(key, _0x23a392)
    headers1['Cookie'] = arg2
    res = requests.get(base_url, headers=headers1)
    # print(res.text)
    if res.status_code==200:
        return res.text





