for x in range(2,1000):
    for y in range(2,x):
        c=(x**2+y**2)**(1/2)
        if x+y+c==1000:
            print(x,y,int(c))
            