import random
classroom = [[],[],[]]
teacher = ['A','B','C','D','E','F','G','H']
for i in teacher:
    j = random.randint(0,2)
    classroom[j].append(i)
print(classroom)
