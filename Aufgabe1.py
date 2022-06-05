z=0
while z<=100:
    if z%3==0 and z%5==0:
        print("3und5teilbar")
    elif z%3==0:
        print("3teilbar")
    elif z%5==0:
        print("5teilbar")
    else:
        print(z)
    z=z+1