from io import StringIO

f = StringIO()
f.write('hello')
f.write('  ')
f.write('world!')
print(f.getvalue())
# 读取 StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
