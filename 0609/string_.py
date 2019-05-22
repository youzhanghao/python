# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:  Reworld

from string import Template



def intString():
    aString = 'hello world'
    print(aString)
    b = str(range(4))
    print(b[1])
    # b[2] = aString  单个字符你只能做访问操作  因其不可变性
    # del b[3]
    print(b)

def compareString():
    a = 'afc'
    b = 'aef'
    # ord(chr) 获取Ascii chr(asc) 获取对应字符
    # 比较 从第一位开始比较ASCII 相同则继续往下一位比较
    if a < b:
        print('a < b')
    else:
        print('a >= b')
def conncetString():
    print('%s %s' % ('Spanish','China'))
    # Spanish China
    s = ' '.join(('Spanish','China')).upper()
    print(s)
    # SPANISH CHINA
    f = ('http://'
         'localhost'
         ':8000'
         '/cgi-bin/friend.py')
    print(f)
    # http://localhost:8000/cgi-bin/friend.py
    a = '您好'
    print(a)
    b = 'hello' 'world'
    print(b)

def stringFormat():
    #  元组类型的参数作为转换
    print("MM/DD/YY = %02d/%02d/%d" % (2, 15, 67))
    w, p = 'Web', 'page'
    print('http://xxx.yyy.zzz/%s/%s.html' % (w,p))
    # MM / DD / YY = 02 / 15 / 67
    # http: // xxx.yyy.zzz / Web / page.html
    # 字典类型的参数提供给格式化操作符
    s1 = 'There are %(howmany)d %(lang)s Quotation Symbols ' % \
        {'lang':'Python','howmany':3}
    print(s1)
    # There are 3 Python Quotation Symbols
    # 注意此处犯了一个错误，文件命名为string.py 导致找不到template  文件命名不要和内建模块重名
    s2 = Template('There are ${howmany} ${lang} Quotation Symbols ')
    # key不存在 keyError异常
    s3 =  s2.substitute(lang='Python',howmany=3)
    print(s3)
    # There are 3 Python Quotation Symbols
    print(s2.safe_substitute(lang='python'))
    # There are ${howmany} python Quotation Symbols

if __name__ == "__main__":
    # intString()
    # compareString()
    # print(string.digits)
    # conncetString()
    # stringFormat()
    a = 'ab'
    b = 'cd'
    print(a+b)