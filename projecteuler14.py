max=0
for x in range(1,1000001):
    count=0
    y=x
    while y!=1:
        if y%2==0:
            y=y/2
            count+=1
        else:
            y=3*y+1
            count+=1
    if max<count:
        max=count
        res=x
print(res)
print(max)
        