#p1-odd even index
#approach-1
"""str=input()
m=""
n=""
for i in range(len(str)):
    if i%2!=0:
        n=n+str[i]
    else:
        m=m+str[i]
print(n+m)
        
"""
#approach-2
"""

str=input()
odd=str[1::2]
even=str[::2]
print(odd+even)
"""
#approach-3
"""
str=input()
print(str[1::2]+str[::2])
"""

#p2-char occurence
#approach-1
"""
str=input()
c=0
ch=input()
for i in range(len(s)):
    if s[i]==ch:
        c=c+1
print(c)
"""
#approach-2
"""
str=input()
c=0
ch=input()
for i in s):
    if i==ch:
        c=c+1
print(c)
"""
#approach-3
"""
str=input()
ch=input()
print(str.count(ch))

"""
#p3-count even index
#approach-1
"""

str=input()
c=0
ch=input()
for i in range(len(s)):
    if s[i]==ch and i%2==0:
        c=c+1
print(c)
"""

#p4-vowels in string
#approach-1-based on vowels count
"""
str=input()
vow="aeiouAEIOU"
count=0
for i in str:
    if i in vow:
        count+=1
    else:
        count
if count==len(str):
    print("Yes")
else:
    print("No")
"""
#approach-2-consonants count
'''
str=input()
vow="aeiouAEIOU"
cos=0
for i in str:
    if i not in vow:
        cos+=1
if cos==0:
    print("Yes")
else:
    print("No")
'''
#approach-3
'''
str=input()
vow="aeiouAEIOU"
for i in str:
    if i not in vow:
        print("No")
        break
else:
    print("Yes")
'''
#p5-digits in string
#approach-1-digits pov
'''
str=input()
dig="0123456789"
count=0
for i in str:
    if i in dig:
        count+=1
if count==len(str):
    print("Yes")
else:
    print("No")
'''
#approach-2-alpha pov
'''
str=input()
dig="0123456789"
alph=0
for i in str:
    if i not in dig:
        alph+=1
if alph==0:
    print("Yes")
else:
    print("No")
    '''
#approach-3-dig pov
'''
str=input()
dig="0123456789"
count=0
for i in str:
    if i not in dig:
        print("No")
        break
else:
    print("Yes")
    '''
#approach-4-built in method
'''
str=input()
print(str.isdigit())

'''
#approach-5
'''
s,ctr=input()
if str.isdigit():
    print("yes")
else:
     print("no")
'''
#p6-count vow,cons
#approach-1
'''
str=input()
v=0
c=0
vow="aeiouAEIOU"
for i in str:
    if i in vow:
        v+=1
    else:
        c+=1
print(v,c)

'''
#approach-2
'''
str=input()
str=str.lower()
v=0
c=0
d=0
vow="aeiouAEIOU"
cons="bcdfghjklmnpqrstvwxyz"
for i in str:
    if i in vow:
        v+=1
    elif i in cons:
        c+=1
print(v,c)
'''
#approach-3
'''
str=input()
str=str.lower()
v=0
c=0
vow="aeiouAEIOU"
for i in str:
    if i.isalpha():
        if i in v:
            v+=1
        else:
            c+=1
print(v,c)
'''
#p7-compress string
#approach-1
'''
s=input()
c=1
r=""
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        c=c+1
    else:
        r=r+s[i-1]
        r=r+str(c)
        c=1
r=r+s[len(s)-1]+str(c)
print(r)
'''
#p8-count words,vowels,consonants
#approach-1
'''

t=int(input())
v="aeiouAEIOU"
for i in range(t):
    s=list(input().split())
    vc=0
    cc=0
    wc=len(s)
    for j in s:
        for k in j:
            if k.isalpha():
                if k in v:
                    vc=vc+1
                else:
                    cc=cc+1
    print(wc,vc,cc)
                    
'''
#approach-2
'''
t=int(input())
v="aeiouAEIOU"
for i in range(t):
    s=input()
    vc=0
    cc=0
    for j in s:
            if j.isalpha():
                if j in v:
                    vc=vc+1
                else:
                    cc=cc+1
    wc=len(s.split())
   print(wc,vc,cc)
'''
#p9-guess the problem
#approach-1
'''
for i in range(int(input())):
    A=input().split()
    for i in A[1]:
        if i in A[0]:
            A[1]=A[1].replace(i,"")
    print(A[1])
    '''
#approach-2
'''
for i in range(int(input())):
    a,b=input().split()
    r=""
    for j in b:
        if j not in a:
            r=r+j
    print(r)
    '''
#p10
#approach-1
for i in range(int(input())):
               s,n=input().split()
               n=int(n)
               r=""
               for i in s:
                   k=ord(i)+n
                   if k>122:
                      k=96+(k-122)
                      r=r+chr(k)
                   else:
                      r=r+chr(k)
               print(r)
#OOPS
#P11
'''
class cse:
    def hello(self):
        print("Hello cse")
class aiml:
    def hello(self):
        print("Hello aiml")
ob1=cse()
ob1.hello()
'''
#P12
'''
class classa:
    def factorial(self,n):
        r = 1
        for i in range(1,n+1):
            r = r * i
        print(r)
ob = classa()
ob.factorial(5)
'''
#P13
'''
class a:
    def __init__(self):
        print("Hello")
    def hello(self):
        print("Hello a")
ob = a()
'''
#P14
'''
class classa:
    def __init__(self,n):
        self.n = n
        print(n)
    def factorial(self):
        r = 1
        for i in range(1,self.n+1):
            r = r * i
        print(r)
ob = classa(5)
ob.factorial()
'''
#P15
'''
class classa:
    def __init__(self,n):
        self.n = n
    def factorial(self):
        print(self.fact(self.n))
    def fact(self,n):
        if n == 1:
            return 1
        else:
            return n * self.fact(n-1)
ob = classa(5)
ob.factorial()
'''

                   
               
               
               
               
               
