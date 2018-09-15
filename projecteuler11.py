prime = [True for i in range(2000000+1)]
p = 2
while (p * p <= 2000000):
         
    if (prime[p] == True):
             
        for i in range(p * 2, 2000000+1, p):
            prime[i] = False
    p += 1

sum=0    
for p in range(2,2000000):
    if prime[p]:
        sum+=p
print(sum)