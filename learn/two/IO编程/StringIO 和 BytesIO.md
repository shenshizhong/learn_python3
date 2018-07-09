# StringIO
##### 除了在文件中读写，也可以在内存中进行读写。
StringIO 指的就是在内存中读写str
使用方法很简单，直接创建一个对象 StringIO，然后调用函数写入即可：

```
from io import StringIO

f = StringIO()
f.write('hello')
f.write('  ')
f.write('world!')
print(f.getvalue())
```
运行结果：
```
hello  world!
```

读取方式：
```
from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
```
运行结果：

```
Hello!
Hi!
Goodbye!
```

##### ByteIO

写入方式：
```
from  io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
```
输出结果：
```
b'\xe4\xb8\xad\xe6\x96\x87'
```
读取方式：
```
from io import BytesIO

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())

```
输出结果：
```
b'\xe4\xb8\xad\xe6\x96\x87'
```

