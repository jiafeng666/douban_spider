from urllib import request, error
from bs4 import BeautifulSoup
import re
import xlwt
import sqlite3

# 影片链接
findlink = re.compile(r'<a href="(.*?)">')
# 影片图片
findimg = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S让换行符包含在字符串中
# 影片名
findtitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findrating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findnums = re.compile(r'<span>(\d*)人评价</span>')
# 影片概况
findinq = re.compile(r'<span class="inq">(.*)</span>')
# 相关信息
findbd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取网页
def getDate(baseurl):
    datalist = []
    for i in range(0, 10):  # 调用获取页面信息的函数10次
        url = baseurl + str(25 * i)
        html = askURL(url)  # 保存获取到的网页源码

        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_='item'):  # 查找符合要求的字符串，生成列表
            # print(item)  # 测试，查看电影item全部信息
            data = []
            item = str(item)
            link = re.findall(findlink, item)[0]  # [0]表示文本，没有[0]显示的格式是数组
            data.append(link)   # 链接

            img = re.findall(findimg, item)[0]
            data.append(img)  #图片

            title = re.findall(findtitle, item)
            if len(title) == 2:
                ctitle = title[0]   #中文名
                data.append(ctitle)
                otitle = title[1].replace("/", "")  #英文名,去掉无关符号
                data.append(otitle)
            else:
                data.append(title[0])
                data.append(' ')  #外国名字留空

            rating = re.findall(findrating, item)[0]
            data.append(rating)  #评分

            nums = re.findall(findnums, item)[0]
            data.append(nums)  #评价数

            inq = re.findall(findinq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)  #概述
            else:
                data.append(" ")

            bd = re.findall(findbd, item)[0]
            bd = re.sub("<br(\s+)?/>(\s+)?", "", bd)
            bd = re.sub("/", " ", bd)
            data.append(bd.strip())

            datalist.append(data)

    return datalist


# 得到一个指定url的页面内容
def askURL(url):
    headers = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77"
    }
    # 用户代理，（伪装）告诉豆瓣服务器我们是什么类型的机器、浏览器（本质上是告诉服务器，我们可以接收什么水平的文件内容）

    req = request.Request(url, headers=headers)
    html = ""
    try:
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
        # print(html)
    except error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)

    return html


# 保存数据
def saveData(datalist, savepath):
    print("save...")
    book = xlwt.Workbook(encoding='utf-8',style_compression=0)   #创建workbook对象
    sheet = book.add_sheet('豆瓣电影top250', cell_overwrite_ok=True)   #创建工作表
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外文名", "评分", "评价人数", "概述", "相关信息")
    for i in range(8):
        sheet.write(0, i, col[i])  #列名
    for i in range(250):
        print("第%d条" % (i+1))
        data = datalist[i]
        for j in range(8):
            sheet.write(i+1, j, data[j])    # 数据

    book.save(savepath)


# def saveData2DB(datalist, dbpath):
#     init_db(dbpath)
#     coon = sqlite3.connect(dbpath)
#     cur = coon.cursor()
#
#     for data in datalist:
#         for index in range(len(data)):
#             if index == 4 or index ==5:
#                 continue
#             data[index] = '"'+data[index]+'"'
#         sql = '''
#             insert into top250movie (
#             info_link,pic_link,Chinese name,Foreign name,rating,nums,introduction,db)
#             values('%s')''' % ",".join(data)
#         cur.execute(sql)
#         coon.commit()
#     cur.close()
#     coon.close()
#
#
# def init_db(dbpath):
#     sql = '''
#         create table top250movie
#         (id integer primary key autoincrement,
#         info_link text,
#         pic_link text,
#         Chinese name varchar,
#         Foreign name varchar,
#         rating numeric,
#         nums numeric,
#         introduction text,
#         db text
#         )
#     '''  # 创建数据表
#     coon = sqlite3.connect(dbpath)
#     cursor = coon.cursor()
#     cursor.execute(sql)
#     coon.commit()
#     coon.close()


def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getDate(baseurl)
    savepath = "豆瓣电影top250.xls"
    saveData(datalist, savepath)
    # dbpath = "movie.db"
    # saveData2DB(datalist, dbpath)


if __name__ == '__main__':
    main()
    #init_db("movietest.db")
    print("爬取完毕！")