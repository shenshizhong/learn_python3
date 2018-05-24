定义一个Student类：
```
>>> class Student(object):
...     pass
...
```

给bart 赋值一个对象：
```
>>> bart = Student()
>>> bart
```
给对象绑定属性：
```
>>> bart.name = "ssz"
>>> bart.name
'ssz'
```
以上就是创建一个python类了。

下面是介绍，在创建类的同时，将要初始化的参数一块传进去，一起绑定创建。
创建类的同时初始化一些参数：
```
>>> class Student(object):
...     def __init__(self, name, age):
...             self.name = name
...             self.age = age
...
>>> bart = Student('ssz', 24)
>>> bart.name
'ssz'
>>> bart.age
24
>>>
```

init 两边分别是两个下划线（两边共4个下划线）
init 的第一个参数self，只能是self。在创建类的时候，第一个默认（不需要传了），只需要传第二个和第三个参数就可以了
通过这样子，我们就能创建一个python的类了。
题外话，之前还有一些知识没写，一开始就写类，会有点突然。有时间的话，后面会把之前没有写的慢慢补充回来，不经过之前的知识也都比较简单。不写的话，大家应该也能获取到那些知识。这些也是我自己学习过程中记录下来的学习笔记而已。

作者：twoP
链接：https://juejin.im/post/5ace271ef265da23a4052e9b
来源：掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。