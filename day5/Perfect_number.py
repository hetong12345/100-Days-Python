i=1
while True:
    i+=1
    res=0
    for x in range (1,i):
        if (i%x)==0 :
            res+=x
    if res==i:
        print(i)