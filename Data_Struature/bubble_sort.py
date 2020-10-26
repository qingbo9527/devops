'''冒泡排序'''
def bub_sort(alist):
    n = len(alist)
    for j in range(n-1):
        for i in range(0,n-1-j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bub_sort(li)
    print(li)
# for j in range(len(alist)-1,0,-1):
# 最优时间复杂度O(n)
def bub_sort(alist):
    n = len(alist)
    for j in range(n-1):
        count = 0
        for i in range(0,n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if 0 == count:
            return
if __name__ == '__main__':
    li = [1, 2, 3, 4, 5, 6]
    print(li)
    bub_sort(li)
    print(li)
