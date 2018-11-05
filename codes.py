import requests
import hashlib
import time
import random


def get_salt():
    salt = (int(time.time()*1000)) + (random.randint(0, 10))
    return salt


def get_md5(v):
    md5 = hashlib.md5()
    md5.update(v.encode('utf-8'))
    sign = md5.hexdigest()
    return sign


def get_sign(keyy, sal):
    sign = 'fanyideskweb' + keyy + str(sal) + '6x(ZHw]mwzX#u0V7@yfwK'
    sign = get_md5(sign)
    return sign


def youdao(key):

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    # url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    # 如果有 _o 的存在，则会报错
    # 去掉的话就可以正常使用了

    sal = get_salt()

    data = {
        'action': 'FY_BY_REALTIME',
        'client': 'fanyideskweb',
        'doctype': 'json',
        'from': 'AUTO',
        'i': key,
        'keyfrom': 'fanyi.web',
        'salt': str(sal),
        'sign': get_sign(key, sal),
        'smartresult': 'dict',
        'to': 'AUTO',
        'typoResult': 'false',
        'version': '2.1'
    }

    # data = urllib.parse.urlencode(data).encode()
    head = {
            'Accept': 'application / json, text / javascript, * / *; q = 0.01',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;q = 0.8, zh - TW;q = 0.7, zh - HK;q = 0.5, en - US;q = 0.3, en;q = 0.2',
            'Connection': 'keep - alive',
            'Content - Length': str(len(data)),
            'Content - Type': 'application/x-www-form-urlencoded;charset = UTF - 8',
            'Cookie': 'YOUDAO_MOBILE_ACCESS_TYPE=1; OUTFOX_SEARCH_USER_ID=-1087170847@10.169.0.84; JSESSIONID=aaa6'
                      '5Zh4PIUybhDi8iKBw; ___rl__test__cookies=1541425927360; OUTFOX_SEARCH_USER_ID_NCOO=18609637'
                      '02.1775036; fanyi-ad-id=52077; fanyi-ad-closed=1',
            'Host': 'fanyi.youdao.com',
            'Referer': 'http: // fanyi.youdao.com /',
            'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
            'X - Requested - With': 'XMLHttpRequest'
    }

    resp = requests.post(url, headers=head, data=data)
    resp.encoding = 'utf-8'
    # res = resp.json()
    print(resp.text)


youdao('crawl')
