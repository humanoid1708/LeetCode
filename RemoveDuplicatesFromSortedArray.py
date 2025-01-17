num = [1,1,3,4,5,5,5,6,7,7,7,7,8,8,9,9,9]
l1 = []
for i in range(len(num)):
    if num[i] not in l1:
        l1.append(num[i])
num = l1
print(num)