# """
# BeautifulSoup4将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:
# • Tag
# • NavigableString
# • BeautifulSoup
# • Comment
# """
#
from bs4 import BeautifulSoup
import re

file = open("./baidu.html", 'rb')  # 二进制读取
html = file.read()
bs = BeautifulSoup(html, "html.parser")
#
# print(bs.title)
# print(bs.a.string)
#print(bs.head)
# # 1.Tag  标签以及内容，默认只取第一个找到的内容
#
# print(bs.title.string)
# print(type(bs.title.string))
# # --> <class 'bs4.element.NavigableString'>
# # 2. NavigableString  标签里的内容（字符串）
#
# print(bs.a.attrs)  # 返回一个包含a标签所有属性的字典
# # --> {'class': ['mnav'], 'href': 'http://news.baidu.com', 'name': 'tj_trnews'}
#
# print(type(bs))
# # --> <class 'bs4.BeautifulSoup'>
# # 3. BeautidulSoup 表示整个文档
#
# print(bs.a.string)
# print(type(bs.a.string))
# # --> <class 'bs4.element.Comment'>
# # 4. Comment，是一个特殊的NavigableString，输出的内容不包含注释符号
#
# # ------------------------------------
#
# # 文档的遍历
# print(bs.head.contents)  # 返回包含标签内容的列表
# print(bs.head.contents[1])  # 指定位置
#
# # 更多内容，搜索文档
#
# # 文档的搜索
# # 1. ①find_all   # 字符串过滤，会查找与字符串完全匹配的内容
# t_list = bs.find_all('a')
# print(t_list)
#
# # # ②正则表达式搜索，使用search()方法来匹配包含内容的整个标签
# t_list = bs.find_all(re.compile('a'))
# print(t_list)
#
#
# # ③ 自定义函数
# def name_is_exits(tag):
#     return tag.has_attr('name')
#
#
# t_list = bs.find_all(name_is_exits)
#
# for i in t_list:
#     print(i)
#
# # 2. kwargs 参数
# t_list = bs.find_all(id='head')
# t_list = bs.find_all(class_=True)
# print(t_list)
#
# # 3.text参数
# t_list = bs.find_all(text=re.compile('\d'))  # 应用正则表达式来查找包含特定文本的内容（标签中的字符串）
# print(t_list)
#
# # 4.limit参数
# t_list = bs.find_all('a', limit=3)
# print(t_list)
#
# # 5.css选择器
# t_list = bs.select('title')  # 通过标签查找
# t_list = bs.select('.mnav')  # 通过类名查找
# t_list = bs.select('#u1')  # 通过id查找
# t_list = bs.select("a[class='bri']")  # 通过属性查找
# t_list = bs.select("head>title")  # 通过子标签来查找
# for item in t_list:
#     print(item)
#
# t_list = bs.select(".mnav ~ .bri")
# print(t_list[0].get_text())


# def name_is_exists(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exists)
# for item in t_list:
#     print(item)

# t_list = bs.find("title")
# print(t_list)