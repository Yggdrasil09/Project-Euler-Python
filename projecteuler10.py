sum=0
for x in range(2,2000000):
    check=0
    for y in range(2,x):
        if x%y==0:
            check=1
            break
    if check==0:
        sum+=x
print(sum)