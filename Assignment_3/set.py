#multiple values
#unordered \ can add and remove items
#unchangeable,unindexed,with curly brackets
#empty set cannot be declared
#duplicates not allowed
#True and 1 is considered same
s={2,'hi',3,'cutie',4,'pie',1,"true"}
print(s)

s.add("mango")
print(s)
#union
s1={"apple","banana"}
s2={1,2,3}
print(s1.union(s2))
s3=s2|s1
print(s3)
#intersection
s1=set()  #create empty set
s2=set()
for i in range(5):
    s1.add(i)
for i in range(3,9):
    s2.add(i)
s3=s1.intersection(s2)   #METHOD ONE
print(s3)
s4=s1&s2        #METHOD TWO
print(s4)

#FIND DIFFERENCE
s1=set()  #create empty set
s2=set()
for i in range(5):
    s1.add(i)
for i in range(3,9):
    s2.add(i)
s3=s1.difference(s2)   #METHOD ONE
print(s3)
s4=s1-s2        #METHOD TWO
print(s4)

#clearing Python set
s4.clear()
print(s4)