import time


def grayCode(n):
    list1=[]
    for i in range(0,1<<n) :
        list1.append(i^(i>>1))
    return list1




if __name__ == '__main__':
    m=int(input('please input the number your want to get:'))
    start = time.clock()
    list=grayCode(m)
    end = time.clock()
    print((list))
    # for i in list:
        # print(bin(i))
    print("final is in ", round(end - start, 6), 's')

