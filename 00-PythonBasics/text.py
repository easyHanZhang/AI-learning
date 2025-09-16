import re

#定义了一个名为is_valid_identifier的函数，该函数接受一个参数name，用于检查该参数是否是一个有效的Python标识符
def is_valid_identifier(name):
    try:
        # 使用正则表达式检查是否为有效的标识符
        if not isinstance(name, str):
            raise ValueError("输入必须是一个字符串")
        #使用re.match函数来检查name是否匹配正则表达式^[a-zA-Z_][a-zA-Z0-9_]*$。
        #该正则表达式的含义是：^ 表示字符串的开始。[a-zA-Z_] 表示标识符的第一个字符必须是字母（大小写均可）或下划线。
        #[a-zA-Z0-9_]*$ 表示标识符的其余部分可以是任意数量的字母、数字或下划线，并且到达字符串的结尾。如果name匹配该正则表达式，则返回True，表示这是一个有效的标识符；否则返回False。
        if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name):
            return True
        else:
            return False
        #第一个处理ValueError异常，如果是这种类型的异常，打印错误信息并返回False。
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return False
        #第二个处理所有其他类型的异常，打印错误信息并返回False。
    except Exception as e:
        print(f"发生了一个意外的错误: {e}")
        return False

print(is_valid_identifier("2var"))  # False
print(is_valid_identifier("var2"))  # True

#保留字即关键字，我们不能把它们用作任何标识符名称。
#Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：
import keyword
keyword.kwlist



#!/usr/bin/python3
 
str='123456789'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第六个的字符（不包含）
print(str[2:])             # 输出从第三个开始后的所有字符
print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)             # 输出字符串两次
print(str + '你好')         # 连接字符串
 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


#!/usr/bin/python3
#print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""
x="a"
y="b"
# 换行输出
print( x )
print( y )
 
print('---------')
# 不换行输出
print( x, end="这里可以加任何结束字符会替代换行" )
print( y, end="" )
print()

print(2 ** 3)
