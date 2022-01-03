str1 = 'hello world'
print(f'字符串的长度为{len(str1)}')

list1 = [1,2,3,45,6,2]
print(f'列表的长度为{len(list1)}')

tuple1 = (1,2,34,6)
print(f'元组的长度为{len(tuple1)}')

set1 = {5,1,2,3,4}

set1.pop()
print(set1)

del list1[1]
print(list1)

for i in str1:
    print(i,end='')
print('')
print(max(tuple1))

print(list(set1))

print(list(str1))