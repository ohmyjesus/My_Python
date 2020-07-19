# *-* coding:UTF8 *-*  在python2中可支持中文字符

#     -------------------1.关于import的语法 import/import .. as ../from .. import ../from .. import ..as../from .. import *
import test1
import test1 as test
from test1 import Dog
from test1 import say_hello
say_hello()
dog = Dog()
print(dog)

#       -----------------------2.在导入模块文件时，文件中没有任何缩进的代码都会被执行一遍，因为测试代码不需要被执行，可采用__name__内置方法实现
import test1
print('-'*50)

#      -------------------------3.包的封装 需要创建package 其下必须包含__init__.py文件 并在init方法中import对外界提供的模块
import package
package.send_message.send("xyh")

a = input("a number: ")
print((a))





