def aufgabe2(a,b,c):
    sum=0
    temp=0
    while(b>0):
        sum=sum+a
        b=b-1
    temp=sum
    c=c-1
    while(c>0):
        sum+=temp
        c=c-1
    return sum

d=aufgabe2(2,3,4)
print(d)