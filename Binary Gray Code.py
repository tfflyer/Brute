"""
反射格雷码的减一生成法
"""


class GrayCode():
    def getGray(self, n):
        global maxn
        maxn = n
        return GrayCode.getGrace(self, ['0', '1'], 1)

    def getGrace(self, list_grace, n):
        global maxn
        if n >= maxn:
            return list_grace
        list_befor, list_after = [], []
        for i in range(len(list_grace)):
            list_befor.append('0' + list_grace[i])
            list_after.append('1' + list_grace[-(i + 1)])
        return GrayCode.getGrace(self, list_befor + list_after, n + 1)


if __name__ == '__main__':
    n = input('Please input the number:')
    n = int(n)
    gary = GrayCode()
    print(gary.getGray(n))
