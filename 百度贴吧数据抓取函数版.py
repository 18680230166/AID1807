import ssl
import urllib.request
import urllib.parse


# 读取页面
def readPage(url):
    context = ssl._create_unverified_context()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req, context=context)
    html = res.read().decode("utf-8")
    return html


# 写入文件
def writePage(filename, html):
    with open(filename, "w", encoding="gb18030") as f:
        f.write(html)
        print("写入成功")


# 主函数
def workOn():
    name = input("请输入贴吧名:")
    begin = int(input("请输入起始页:"))
    end = int(input("请输入终止页:"))
    # 对贴吧名name进行编码
    kw = {"kw": name}
    kw = urllib.parse.urlencode(kw)
    # 拼接URL,发请求,获响应
    for i in range(begin, end + 1):
        # 拼接URL
        pn = (i - 1) * 50
        baseurl = "http://tieba.baidu.com/f?"
        url = baseurl + kw + "&pn=" + str(pn)
        html = readPage(url)
        filename = "第" + str(i) + "页.html"
        writePage(filename, html)


if __name__ == "__main__":
    workOn()



























