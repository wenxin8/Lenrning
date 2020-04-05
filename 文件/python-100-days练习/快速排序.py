 # 快速排序
def sort_1(mylist):
    listlen = len(mylist)
    if listlen <= 1:
        return mylist
    mid = listlen // 2
    miditem = mylist[mid]
    mylist.remove(miditem)
    left = []
    right = []
    left = [x for x in mylist if x < miditem]
    right =[x for x in mylist if x >= miditem]
    return sort_1(left) + [miditem] + sort_1(right)

 # 归并排序
def sort_2(mylist):
    listlen = len(mylist)
    if listlen <= 1:
        return mylist
    num = listlen // 2
    left = sort_2(mylist[:num])
    right = sort_2(mylist[num:])
    return merge(left, right)
def merge(left, right):
    result = list()
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


def main():
    n = int(input())
    mylist = list(map(int, input().split()))
    for i in sort_2(mylist):
        print(i, end=' ')
main()
