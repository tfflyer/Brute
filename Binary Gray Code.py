"""
反射格雷码的减一生成法
"""
import time



class GrayCode():

    def getGray(self, n):
        global maxn
        maxn = n
        return GrayCode.getGrace(self, ['0', '1'], 1)

    def getGrace(self, list_grace, n):
        # print(list_grace)
        global maxn
        if n >= maxn:
            return list_grace
        list_befor, list_after = [], []
        for i in range(len(list_grace)):
            list_befor.append('0' + list_grace[i])
            list_after.append('1' + list_grace[-(i + 1)])
        return GrayCode.getGrace(self, list_befor + list_after, n + 1)


if __name__ == '__main__':
    n = input('请输入你所希望生成的格雷码的位数:')
    n = int(n)
    start = time.clock()
    gary = GrayCode()
    print(gary.getGray(n))
    end = time.clock()

    print("final is in ", round(end - start, 4), 's')
