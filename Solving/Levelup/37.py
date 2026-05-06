# 37. Sort a list without using sort() (basic logic).

lst=[8,9,1,5,7,10,20,4,3,3,4,5]


for i in range(1, len(lst)):
    key = lst[i]
    j = i - 1

    while j >= 0 and lst[j] > key:
        lst[j + 1] = lst[j]
        j -= 1

    lst[j + 1] = key

print(lst)


