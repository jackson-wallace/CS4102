

a = [1, 1, 1, 1, 2, 1, 1, 1, 1]
mid = (0 + len(a)) // 2
# print(mid)


def biggerSum(l1, l2):
    sum1 = 0
    sum2 = 0
    for val in l1:
        sum1 += val
    for val in l2:
        sum2 += val
    # print(sum1, sum2)
    if l1 > l2:
        return -1
    elif l1 == l2:
        return 0
    else:
        return 1


biggerSum(a[0:mid], a[mid:len(a)])


def find2(a, l, r):

    mid = (l + r) // 2

    l1, l2 = a[l:mid], a[mid:r]

    i = biggerSum(l1, l2)
    if a[mid] == 2:
        return mid
    elif i == -1:
        return find2(a, l, mid-1)
    elif i == 1:
        return find2(a, mid+1, r)
    else:
        if len(l1) - len(l2) > 0:
            return find2(a, mid+1, r)
        else:
            return find2(a, l, mid-1)


print(find2(a, 0, len(a)))
