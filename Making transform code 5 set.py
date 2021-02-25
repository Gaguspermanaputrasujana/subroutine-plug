import time
import sys
from time import sleep

#hashingnumber

a="12345"
b = list(a)

r=[]
for c in b:
    c = int (c)
    if c == 1 or c==3 or c == 5:
        c=c*2+1
        c = str (c)
        r.extend([c])
    else: 
        c=(c+1)*2
        c=str (c)
        r.extend([c])

r="".join(r)
r=list(r)
print(r)
n=0
for x in r:
    n+=1
while n>5:
    r.pop()
    n-=1
r="".join(r)
print(r)