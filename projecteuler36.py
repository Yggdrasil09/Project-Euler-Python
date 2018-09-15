sum=0
for x in range(1,1000000) :
    if str(x)==str(x)[::-1] and str("{0:b}".format(x))==str("{0:b}".format(x))[::-1] :
        sum+=x
print(sum)