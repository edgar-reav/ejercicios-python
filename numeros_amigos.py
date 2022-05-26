def amigos(a,b):
    s_a=0
    s_b=0
    for i in range(1,a):
        if a%i==0:
            s_a+=i
 
    for k in range(1,b):
        if b%k==0:
            s_b+=k
 
    return s_a==b and s_b==a
