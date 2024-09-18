file = open('zadanie24_3.txt').readline()
a=[] #список для хранения индексов крайних элементов последовательности lider
b=[] #список для хранения количества различных символов между ними
for i in range (1,len(file)-4):
    if file[i] == 'l' and file[i + 1] == 'i' and file[i + 2] == 'd' and file[i + 3] == 'e' and file[i + 4] == 'r':
       a.append(i)
       a.append(i+4)
a.pop(0) #потому что перед первым элементом в списке нет другой последовательности
for i in range(0,len(a)-1,2):
    c=set(file[a[i]+1:a[i+1]])
    b.append(len(c))
print(min(b))
print(b)
