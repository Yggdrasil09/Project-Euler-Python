p=1
while True:
    t=int(p*(p+1)/2)
    count=0
    for x in range(1,t+1):
        if t%x==0:
            count+=1
    if count>=500:
        print(p)
        break
    p+=1

