nums = 41
call = 3

peoples = []
for _ in range(nums):
    peoples.append(True)

result = []
num = 1

while (any(peoples)):
    for index, people in enumerate(peoples):
        if people:
            if num == call:
                peoples[index] = False
                result.append(index + 1)
                print(index+1)#每轮的出局者
                # print(peoples)#每次的队列状态
                num = 1
            else:
                num += 1
print('-' * 25)
print('\n总数为%d,报数为%d' % (nums, call))
print('约瑟夫序列为：\n%s\n' % result)
print('-' * 25)