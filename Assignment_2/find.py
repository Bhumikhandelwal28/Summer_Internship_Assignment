lists=[]
n=int(input("Enter the number of elements in the list"))
for i in range(n):
    lis=int(input(f"Enter value at {i+1}"))
    lists.append(lis)
#smallest number

mini=lists[0]
for i in lists:
    if mini>i:
        mini=i
print(mini)


#find second greatest number
new_list=set(lists)
print(new_list)
max1=max(new_list)
new_list.remove(max1)
max2=max(new_list)
print(f"the second greatest number is {max2}")


#find second smallest number
min1=min(new_list)
new_list.remove(min1)
min2=min(new_list)
print(f"the second smallest number is {min2}")

#another way
"""
new_list=list(set(lists))
print(new_list)
new_list.sort(reverse=True)
print(new_list)
print("the second greatest number is:",new_list[1])
"""