import re
import time
from itertools import permutations


def solve(puzzle):
    puzzle = puzzle.upper()                            # 统一转换为大写
    words = re.findall('[A-Z]+', puzzle)               # 提取出字母
    unique_characters = set(''.join(words))
    assert len(unique_characters) <= 10, 'Too many letters'  # 只有0—9十个数
    first_letters = {word[0] for word in words}    # 首字母
    n = len(first_letters)
    sorted_characters = ''.join(first_letters) + \
                        ''.join(unique_characters - first_letters)
    characters = tuple(ord(c) for c in sorted_characters)
    digits = tuple(ord(str(c)) for c in range(10))
    zero = digits[0]     # 数字0不能是第一位
    print('蛮力测试：\n')
    for guess in permutations(digits, len(characters)):
        if zero not in guess[:n]:
            equation = puzzle.translate(dict(zip(characters, guess)))     # 转换字符
            dig = tuple(chr(c) for c in guess)
            if eval(equation):               # 将字符串string对象转化为有效的表达式进行计算
                print(sorted_characters)
                print(dig)
                return equation


if __name__ == '__main__':
    start = time.clock()
    # puzzle = "send + more == money"
    puzzle = input("请输入字母算术式,并用‘==’连接：")
    try:
        print(puzzle.upper())
        solution = solve(puzzle)
        end = time.clock()
        if solution:
            print(puzzle)
            print('符合条件的结果：\n'+solution)
            print("final is in ", round(end - start), 's')
        else:
            print("sorry，这个式子臣妾真的尽力了，找不到结果")
    except Exception as e:
        print("Error: " + str(e))
