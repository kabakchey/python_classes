# list comprehensions
lst = [i for i in range(1,100,2)]
lst = [i**2 for i in range(100)]
lst = [i for i in range(100) if i%2==0]

# add elem
lst = ['a','b','c']
lst.append('d')
# or
lst += 'x'
print(lst)

# sort list in asc./desc. order
lst = [1,2,3,1]
lst.sort()
lst.sort(reverse=True)
print(lst)

# list elem deletion
lst = [1,2,3]
del lst[0]
# or
lst[1:2]=[]
print(lst)

# list elem insertion
lst = [1,2,3]
lst[1:2]=['a','b']
#or
lst.insert(1,'x')
print(lst)

# reverse
lst = [2,0,1,6]
lst.reverse()
# or
lst[::-1]

# deletion the entire list
lst=[1,2,3]
lst*=0
print(lst)
# or
lst=[1,2,3]
lst[:]=[]
print(lst)
# or
lst=[1,2,3]
del lst[:]
print(lst)
# but not
lst=[1,2,3]
del lst
print(L)

# find index
lst=[2,0,1,6]
if 1 in lst:
    print(lst.index(1))
    
# remove by value
lst=[2,0,1,6]
lst.remove(2)
print(lst)

# remove by index
lst=[2,0,1,6]
if 2 in lst:
    del lst[lst.index(2)]
print(lst)
    
# make copy not ref
lst=[2,0,1,6]
def foo(l):
    l[0] = 'x'

print(lst)
foo(lst[:]) # compare with foo(lst)
print(lst)

# functions with lists
lst = [i for i in range(10)]
list_sum = sum(lst)
list_max = max(lst)
list_min = min(lst)
print(list_sum, list_max, list_min)
