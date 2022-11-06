import re


class Stack(object):

    def __init__(self):
        self.stack = []


    def isEmpty(self):
        return self.stack == []


    def peek(self):
        return self.stack[-1]

    def peek1(self):
        return self.stack[-2]


    def size(self):
        return len(self.stack)

    def push(self, item):
        self.stack.append(item)


    def pop(self):
        return self.stack.pop()

    def show(self):
        print(self.stack)


st = Stack()
t1 = 0
t2 = 0
t3 = 0
t4 = 0
flag = 0
total = 0
x = 0
arva = [0 for x in range(10000)]

filename = input()
grade = input()

f = open(filename, "r")
data = f.read()

data = re.sub(r"\"[\S\s]*?\"", "", data)
data = re.sub(r"\/\*[\S\s]*?\*\/", "", data)

res = re.findall(r'\bdo\b', data)
res = re.findall(r'\bauto\b', data)
total += len(res)
res = re.findall(r'\bbreak\b', data)
total += len(res)
res = re.findall(r'\bcase\b', data)
total += len(res)
res = re.findall(r'\bchar\b', data)
total += len(res)
res = re.findall(r'\bconst\b', data)
total += len(res)
res = re.findall(r'\bcontinue\b', data)
total += len(res)
res = re.findall(r'\bdefault\b', data)
total += len(res)
res = re.findall(r'\bdouble\b', data)
total += len(res)
res = re.findall(r'\belse\b', data)
total += len(res)
res = re.findall(r'\benum\b', data)
total += len(res)
res = re.findall(r'\bextern\b', data)
total += len(res)
res = re.findall(r'\bfloat\b', data)
total += len(res)
res = re.findall(r'\bfor\b', data)
total += len(res)
res = re.findall(r'\bgoto\b', data)
total += len(res)
res = re.findall(r'\bif\b', data)
total += len(res)
res = re.findall(r'\bint\b', data)
total += len(res)
res = re.findall(r'\blong\b', data)
total += len(res)
res = re.findall(r'\bregister\b', data)
total += len(res)
res = re.findall(r'\breturn\b', data)
total += len(res)
res = re.findall(r'\bshort\b', data)
total += len(res)
res = re.findall(r'\bsigned\b', data)
total += len(res)
res = re.findall(r'\bsizeof\b', data)
total += len(res)
res = re.findall(r'\bstatic\b', data)
total += len(res)
res = re.findall(r'\bstruct\b', data)
total += len(res)
res = re.findall(r'\bswitch\b', data)
total += len(res)
t1 = len(res)
res = re.findall(r'\btypedef\b', data)
total += len(res)
res = re.findall(r'\bunion\b', data)
total += len(res)
res = re.findall(r'\bunsigned\b', data)
total += len(res)
res = re.findall(r'\bvoid\b', data)
total += len(res)
res = re.findall(r'\bvolatile\b', data)
total += len(res)
res = re.findall(r'\bwhile\b', data)
total += len(res)

f.seek(0)
i = 0
k = len(f.readlines())
f.seek(0)
for i in range(k):
    data = f.readline().strip()

    data = re.sub(r"\"[\S\s]*?\"", "", data)
    data = re.sub(r"\/\*[\S\s]*?\*\/", "", data)

    res = re.findall(r'\bswitch\b', data)
    if flag == 1 and len(res) > 0:
        flag = 2
    if len(res) > 0 and flag == 0:
        flag = 1
    if flag == 1:
        res = re.findall(r'\bcase\b', data)
        t2 = t2 + len(res)
        res = re.findall(r'\bdefault\b', data)
        if len(res) > 0:
            flag = 0
            arva[x] = t2
            x = x + 1
            t2 = 0
    if flag == 2:
        flag = 1
        arva[x] = t2
        x = x + 1
        t2 = 0
    if i == k - 1 and t2 != 0:
        arva[x] = t2
        x = x + 1
        t2 = 0

f.seek(0)
k = len(f.readlines())
f.seek(0)
for i in range(k):
    data = f.readline().strip()

    data = re.sub(r"\"[\S\s]*?\"", "", data)
    data = re.sub(r"\/\*[\S\s]*?\*\/", "", data)

    res = re.findall(r'\bif\b', data)
    res1 = re.findall(r'\belse\b', data)
    res2 = re.findall(r'{', data)
    res3 = re.findall(r'}', data)

    if (len(res) > 0) and (len(res1) == 0):
        st.push(1)  # 1入栈
    if (len(res) > 0) and (len(res1) > 0):
        st.push(2)  # 2入栈
    if (len(res1) > 0) and (len(res) == 0):
        if st.isEmpty() == False and st.peek() == 2:
            t4 = t4 + 1
            while st.peek() == 2:
                st.pop()
            st.pop()
        if st.isEmpty() == False and st.peek() == 1:
            t3 = t3 + 1
            st.pop()
    if (len(res2) > 0):
        st.push(3)
    if (len(res3) > 0):
        if st.isEmpty() == False and st.peek() == 3:
            st.pop()
        elif (st.isEmpty() == False and st.peek() == 2) or (st.isEmpty() == False and st.peek() == 1):
            while st.peek() != 3:
                st.pop()
            st.pop()

key = int(grade)

if key == 1:
    print('total num:', end=' ')
    print(total)
    print('switch num:', end=' ')
    print(t1)
if key == 2:
    print('total num:', end=' ')
    print(total)
    print('switch num:', end=' ')
    print(t1)
    print('case num:', end=' ')
    for i in range(x):
        if arva[i] != 0:
            print(arva[i], end=' ')
    print()
if key == 3:
    print('total num:', end=' ')
    print(total)
    print('switch num:', end=' ')
    print(t1)
    print('case num:', end=' ')
    for i in range(x):
        if arva[i] != 0:
            print(arva[i], end=' ')
    print()
    print('if-else num:', end=' ')
    print(t3)
if key == 4:
    print('total num:', end=' ')
    print(total)
    print('switch num:', end=' ')
    print(t1)
    print('case num:', end=' ')
    for i in range(x):
        if arva[i] != 0:
            print(arva[i], end=' ')
    print()
    print('if-else num:', end=' ')
    print(t3)
    print('if-elseif-else num:', end=' ')
    print(t4)

f.close()