def order1(a):
    #checking condition
    #if len(a) != len(set(a)) and not (1<len(a)<100):
        #exit()
    #checking ascending lists
    if a[0]>a[1]:
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                continue
            else:
                return "not sorted"
        return "descending"
    #checking descending lists
    if a[0]<a[1]:
        for i in range(len(a)-1):
            if a[i]<a[i+1]:
                continue
            else:
                return"not sorted"
        return "ascending"

print(order1([6, 20, 160, 420]))
print(order1([23,47,797]))
print(order1([430,200,23,3]))