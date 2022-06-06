def aufgabe2(a,b,c):
    sum=0  #Da eine multiplikation eigentlich nur eine Summe ist von a die b mal wiederholt wird 
    temp=0 #und c nur eine wiederholung vom vorherigen Ergebnis lässt sich das Ergebnis in Zwei Schleifen hier einfach erklären.
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