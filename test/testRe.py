import re

# 创建模式对象
# pat = re.compile("aa")
# m = pat.search("ddfdwwqaa")
# print(m)

# 不用创建模式对象
# m = re.search('aa', 'dfdaaddf')   #前面的为匹配模板，后面为校验内容
# print(m)

#findall
# print(re.findall('[a-z]', 'sfdsrDHFN'))
# print(re.findall('[a-z]+', 'sfdsrDHFN'))

#sub
#print(re.sub('bb', 'aa', 'aabbcc'))  #bb为被替换，aa为替换成的

# 正则表达式中，在被比较的字符串前面加上r,不用担心转义字符的问题
# print(r"dfdg\t")

pat=re.compile('\.')
print(pat.findall('abc.efg'))