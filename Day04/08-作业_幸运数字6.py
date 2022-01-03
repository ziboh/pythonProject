num = int(input('请输入幸运数字：'))
nums = []
lucky = []
for i in range (1,num + 1):
    nums.append(i)
    if i % 6 == 0:
        lucky.append(nums.pop(nums.index(i)))
print(lucky)
print(nums)