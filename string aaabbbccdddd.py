s = "aaabbbccdddd"
a=0
b=0
c=0
d=0
for i in s:
    if 'a' in i:
        a=a+1
        itema = i
    elif 'b' in i:
        b=b+1
        itemb = i
    elif 'c' in i:
        c= c+1
        itemc = i
    elif 'd' in i:
        d= d+1
        itemd = i
print(str(a)+itema+str(b)+itemb+str(c)+itemc+str(d)+itemd)
