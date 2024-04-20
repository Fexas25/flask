def insert(a):
    for i in range(len(a)):
        tem = a[i]
        j = i - 1
        while j>=0 and a[j]>tem:
            a[j+1] = a[j]
            j = j -1
        a[j+1] = tem
    return a

def bubble(a):
    while True:
        change = True
        for i in range(len(a)):
            j = i+1
            if j<=len(a)-1 and a[i]>a[j]:
                mid = a[i]
                a[i] = a[j]
                a[j] = mid
                change = False
        if change == True:
            break
    return a

def merge_sort(left, right):
    tot = []
    l = 0
    r = 0
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            tot.append(left[l])
            l = l+1
        else:
            tot.append(right[r])
            r = r+1
    tot = tot + left[l:]
    tot = tot + right[r:]
    return tot

def merge(a):
    if len(a)<=1:
        return a
    left = merge(a[:len(a)//2])
    right = merge(a[(len(a)//2):])
    return merge_sort(left, right)


def fast(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    fast(array, low, left - 1)

a = [2, 5, 3, 7, 1, 6]
print(fast(a))