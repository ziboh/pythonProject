# 定义列表
# name = 'zhoubohua'
# list1 = ['z','h','o','u','b','o','h','u','a',name]
# print(list1)
# print(type(list1))

fruits = ['apple','banana','orange','apple']
print(fruits.count('apple'))
print(len(fruits))
print(fruits.index('apple'))
if 'apple' in fruits:
    print('apple在列表里')
else:
    print('apple不在列表里')
fruits.append('peach')
print(fruits)
new_fruits = ['pineapple','pear']
fruits.extend(new_fruits)
print(fruits)
pitaya = 'pitaya'
fruits.insert(2,pitaya)
print(fruits)
# 删除操作
del fruits[0]
print(fruits)
print(fruits.pop(2))
print(fruits)
fruits.remove('banana')
print(fruits)
# fruits.clear()
# print(fruits)




# 修改操作
fruits[1] = 'banana'
print(fruits)

nums = [1,3,5,4,11,543,65]
nums.reverse()
print(nums)
nums.sort(reverse= True)
print(nums)
nums.sort()
print(nums)
nums1 = nums
print(nums1)

for i in nums:
    print(i,end='   ')

