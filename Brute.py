import re
import time
from itertools import permutations                  # 全排列的包


def solve(puzzle):
    puzzle = puzzle.upper()                            # 统一转换为大写
    words = re.findall('[A-Z]+', puzzle)               # 提取出字母
    unique_characters = set(''.join(words))
    assert len(unique_characters) <= 10, 'Too many letters'  # 只有0—9十个数
    first_letters = {word[0] for word in words}    # 首字母
    n = len(first_letters)
    sorted_characters = ''.join(first_letters) + \
                        ''.join(unique_characters - first_letters)     # 排序，把首字母放在前面
    characters = tuple(ord(c) for c in sorted_characters)
    digits = tuple(ord(str(c)) for c in range(10))
    zero = digits[0]
    print('蛮力测试：\n')
    for guess in permutations(digits, len(characters)):    # 对十个数字进行全排列
        if zero not in guess[:n]:     # 首字母不为零

            equation = puzzle.translate(dict(zip(characters, guess)))     # 转换字符,用数字替换字母
            dig = tuple(chr(c) for c in guess)

            if eval(equation):               # 判断等式是否成立
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
            print('\n'+solution)
            print("final is in ", round(end - start), 's')
        else:
            print("sorry，这个式子臣妾真的尽力了，找不到结果")
    except Exception as e:
        print("Error: " + str(e))
