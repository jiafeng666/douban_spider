import urllib.request
import urllib.parse  # 解析器
#
# get请求
response = urllib.request.urlopen("https://www.baidu.com")
print(response.getheaders())
print(response.getheader('Date'))
print(response.read().decode('gbk'))
#
# # 获取post请求，模拟登陆
# data = bytes(urllib.parse.urlencode({"13620226479": "123456"}), encoding='utf-8')    #封装post表单信息，字典里传用户名密码，cookie..
# response = urllib.request.urlopen('http://www.jin10.com/', data=data)
# print(response.read().decode('utf-8'))
#
# # 超时处理
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError:
#     print("time out!")

# 伪装成浏览器，访问百度
# url = "https://www.conab.gov.br/info-agro/safras/progresso-de-safra"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77"
# }
# req = urllib.request.Request(url=url, headers=headers)  # 将各种信息封装在 req对象中
# response = urllib.request.urlopen((req))
# print(response.read().decode('utf-8'))

# import requests
# from lxml import etree
# import time
#
#
# def func():
#     url = "https://www.conab.gov.br/info-agro/safras/progresso-de-safra"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77"
#     }
#     response = requests.get(url=url, headers=headers)
#     #print(response)
#     data_txt = response.text
#     #print(data_txt)
#     date = etree.HTML(data_txt)
#     pd_xl = date.xpath('//ul[@class="catItemAttachments"]//li/a')
#     #print(pd_xl)
#     for px in pd_xl:
#         time.sleep(1)
#         px_url = px.xpath('./@href')[0]
#         #print(px_url)
#         Url = ' https://www.conab.gov.br' + px_url
#         name = px.xpath('./@title')[0]
#         print('文件名为: {},链接为: {}'.format(name, Url))
#
#
# if __name__ == '__main__':
#     func()


# import aiohttp
# import asyncio
#
# """
#     aiohttp:发送http请求
#     1.创建一个ClientSession对象
#     2.通过ClientSession对象去发送请求（get, post, delete等）
#     3.await 异步等待返回结果
# """
#
# # get请求
# async def main():
#     url = 'https://www.jin10.com/'
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as res:
#             print(await res.text(encoding='utf-8'))
# loop = asyncio.get_event_loop()
# task = loop.create_task(main())
# loop.run_until_complete(task)
#
#
# # import aiohttp
# # import asyncio
#
# """
#     aiohttp:发送POST请求
# """
# # post请求
# async def main():
#     data = {'key1': 'value1', 'key2': 'value2'}
#     url = 'https://www.jin10.com/'
#     async with aiohttp.ClientSession() as session:
#         async with session.post(url, data=data) as res:
#             print(res.status)
#             print(await res.text(encoding='utf-8'))
# loop = asyncio.get_event_loop()
# task = loop.create_task(main())
# loop.run_until_complete(task)