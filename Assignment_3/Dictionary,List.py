#dictionary
dic={1:"python",2:"java",3:"c++",4:{1:"one",2:"two"}}

print(dic)
print(type(dic))
print(dic[2])
print(dic[4][2])

#adding elements in dictionary

dic[5]="mongodb"
dic[6]="C"
print(dic)
del(dic[4])
print(dic)

#methods
print(dic.items())
dic2=dic.copy()
print(dic2)
dic2.clear()
print(dic2)
print(dic.values())
print(dic.keys())

print(dic)
dic.pop(4)
print(dic)
dic.popitem()
print(dic)
dic2={'hello':2}
dic.update(dic2)
print(dic2)
print(dic)

dict1={'a':10,'b':8}
dict2={'d':6,'c':4}
dict2.update(dict1)
print(dict2)

#tuple is ordered data type
#it is unchangeable
#tuple in round bracket
#allow duplicate items
tup=(10,20,30,20)
print(tup)

print(type(tup))
for x in tup:
    print(x)
for x in range(len(tup)):
    print(tup[x])

for x in range(len(tup)):
    print(x,tup[x])

t1=(0,1,2,3)
t2=('a','b')
print(t1+t2)
t3=(t1,t2)
print(t3)
print(t1,t2)
t=('xyz',)*3  #here comma is necessary for separated strings
print(t)
print(t1[1:3])

tt=(0,1)
del tt

l=[1,2,2,3,4]
t=tuple(l)
print(type(t))

#tuple methods
#min,max,count,index,sum
print(min(t))
print(max(t))
print(sum(t))
# pass an argument
c=t.count(2)
print(c)
print(t.index(3))

