N = int(input("Введите число"))
b=[]
for i in range(N):
    a=int(input())
    b.append(a)
print(b)
b.insert(0, b[0])
b.insert(0, b[N])
b.pop()
b.pop(1)
print(b)
