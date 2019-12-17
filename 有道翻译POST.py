import urllib.request
import urllib.parse
import json

# 请输入要翻译的内容
key = input('请输入要翻译的内容：')

# 把提交的form表单数据转为bytes数据类型
data = {"i": key,
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":"1540373170893",
        "sign":"a5d9b838efd03c9b383dc1dccb742038",
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_REALTIME",
        "typoResult":"false"
    }

# 字符串
data = urllib.parse.urlencode(data)
data = bytes(data,'utf-8')

# 发送请求，获取响应

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers = {'User-Agent':'Mozilla/5.0'}

req = urllib.request.Request(url,data=data,headers=headers)
res = urllib.request.urlopen(req)
html = res.read().decode('utf-8')

r_dict = json.loads(html)
print(r_dict)