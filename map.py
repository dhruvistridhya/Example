ls=[1,2,3,4,5]
ls1=[6,7,8,9,10]

print("list1:",ls)
print("list2",ls1)

s=map(lambda l: l**2,ls)
print(list(s))

s1=map(lambda n1,n2:n1+n2,ls,ls1)
print(list(s1))