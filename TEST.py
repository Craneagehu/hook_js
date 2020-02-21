import requests
import execjs
import js2py
'''
国家企业信用信息公示系统的信息公告 破解cookie=>jsl_clearance
'''
url = "http://www.gsxt.gov.cn/affiche-query-area-info-paperall.html"

querystring = {"noticeType":"11","areaid":"100000","noticeTitle":"","regOrg":""}

payload = "draw=1&start=0&length=10"
# 经过测试可以发现 UA 以及 Cookie 中的 __jsluid_h  __jsl_clearance SECTOKEN or JSESSIONID 都是不可缺少的参数。
headers = {
    'Cookie': "__jsluid_h=aa1c7a0fc461a8ea63747a4b02956b38; __jsl_clearance=1565006542.706|0|D0rZ6Fm9vgqQ2QyKbNgIlZRkMsw%3D; SECTOKEN=6968716378603526401; JSESSIONID=40B833BC895E78C1A2E6C2D74C1DE6F8-n2:2;",
    # 'Origin': "http://www.gsxt.gov.cn",
    # 'Accept-Encoding': "gzip, deflate",
    # 'Accept-Language': "zh-CN,zh;q=0.9",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    }
response = requests.post(url, data=payload, headers=headers, params=querystring)

js_code1 = response.text
js_code1 = js_code1.rstrip('\n')
js_code1 = js_code1.replace('</script>', '')
js_code1 = js_code1.replace('<script>', '')
# print(js_code1) # break}catch(_){}

index = js_code1.rfind('}') # rfind() 返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1。
js_code1 = js_code1[0:index + 1]
print(js_code1)

js_code1 = js_code1.replace('eval', 'return')
js_code1 = 'function getCookie() {' + js_code1 + '}'
print(js_code1)

js_code2 = execjs.compile(js_code1)
code = js_code2.call('getCookie')
print(code)
# 获取cookie索引
index_cookie = code.find('cookie=')
index_if = code.rfind('if')

code2 = code[index_cookie:index_if]
print(code2)
code2 = 'var '+code2[:-2]

cookie = js2py.eval_js(code2)
print(cookie)