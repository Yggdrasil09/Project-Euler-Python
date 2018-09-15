max=0
for x in range(101,1000):
    for y in range(100,x):
        z=str(x*y)
        if z==z[::-1]:
            if max<int(x*y):
                max=int(x*y)
print(max)

            

