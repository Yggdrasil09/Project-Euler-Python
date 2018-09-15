y=2
count=0
while True:
    check=0
    for x in range(2,int(y/2)):
        if y%x==0:
            check=1
    if check==0:
        count+=1
    if count==10002:
        break
    y+=1
print(y)


