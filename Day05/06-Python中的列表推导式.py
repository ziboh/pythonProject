# list1 = [i**2 for i in range(1,10)]
#
# print(list1)
list1 = [i for i in range(1,100) if i % 2 == 0]
print(list1)


list2 = [(i // 3,i % 3) for i in range(3,9)]
print(list2)


list1 = ['name','age','gender']
list2 = ['Tom',18,'male']
# person = {list1[i]:list2[i] for i in range(len(list1))}
print({list1[i]: list2[i] for i in range(len(list1))})

counts ={'MBP':268,'HP':125,'DELL':201,'Lenovo':199,'ACER':99}
nums_up_200 = {i:j for i,j in counts.items() if j >= 200}
print(nums_up_200)


