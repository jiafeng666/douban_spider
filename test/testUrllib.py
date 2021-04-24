import urllib.request
import urllib.parse   # 解析器

# get请求
response = urllib.request.urlopen("http://www.baidu.com")
print(response.getheaders())
print(response.getheader('Date'))
print(response.read().decode('utf-8'))


# 获取post请求，模拟登陆
data = bytes(urllib.parse.urlencode({"hello":"World"}), encoding='utf-8')    #封装post表单信息，字典里传用户名密码，cookie..
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read().decode('utf-8'))

# 超时处理
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.01)
    print(response.read().decode('utf-8'))
except urllib.error.URLError:
    print("time out!")

#伪装成浏览器，访问豆瓣
url = "http://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77"
}
req = urllib.request.Request(url=url, headers=headers)  # 将各种信息封装在 req对象中
response = urllib.request.urlopen((req))
print(response.read().decode('utf-8'))
