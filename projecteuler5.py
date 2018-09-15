count=230000000
while True:
    count1=0
    for x in range(1,21):
        if count%x==0 :
            count1=count1+1
    if count1==20:
        print(count)
        break
    count+=1
        