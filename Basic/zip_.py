"""Iterate over several iterables in parallel, producing tuples with an item from each one."""
l1=[1,2,3,4]
l2=[1,2,3,4]

res=[i+j for i,j in list(zip(l1,l2))]
print(res)