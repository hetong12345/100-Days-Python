for num in range(100,999):
    x=num//100
    y=(num-x*100)//10
    z=num-x*100-y*10
    if x**3+y**3+z**3==num:
        print(x,y,z,num)