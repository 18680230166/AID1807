import urllib.request
import urllib.parse

class BaiduSpider:
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0'}
        self.baseurl = 'http://tieba.baidu.com/f?'

    def readPage(self,url):
        # 请求读取页面
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        return html
    def writePage(self,filename,html):
        with open(filename,'w',encoding='gb18030') as f:
            f.write(html)
            print('写入成功')
    def workOn(self):
        '最终抓取'
        name = input('请输入贴吧名：')
        begin = int(input('请输入起始页：'))
        end = int(input('请输入终止页：'))
        # 对贴吧name进行编码
        kw = {'kw':name}
        kw = urllib.parse.urlencode(kw)
        # 拼接URL，发送请求,获取响应
        for i in range(begin,end+1):
            # 拼接URL
            pn = (i-1)*50
            url = self.baseurl + kw +'&pn='+ str(pn)
            html = self.readPage(url)
            filename = '第'+str(i)+'页.html'
            self.writePage(filename,html)
if __name__ == '__main__':
    spider = BaiduSpider()
    spider.workOn()