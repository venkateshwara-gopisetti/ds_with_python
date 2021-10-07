from array import *
arr1 = array('i', [1,2,3,4,5])

# Traverse/Access
print('Traversing the array')
for i in arr1:
    print(i)

print(arr1[1])


# Insertion
print('before inserting')
print(arr1)
print('inserting at index 1')
arr1.insert(1,10)
print('after insertion')
print(arr1)

# Deletion
arr1.remove(10)
print('deleting value 10 from array')
print(arr1)

# Search
print('find index of value 4')
print(arr1.index(4))

# Update
print('update value 4 to 8')
arr1[arr1.index(4)]=8
print(arr1)