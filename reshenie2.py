file = open('zadanie24_2.txt').readline()
sum = 0
for i in range (1,len(file)-4):
    if file[i]=='l' and file[i+1]=='i' and file[i+2]=='d' and file[i+3]=='e' and file[i+4]=='r':
        sum+=int(file[i-1])
print(sum)