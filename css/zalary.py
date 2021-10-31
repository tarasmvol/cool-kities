def studying_hours(a):
    final_list_hours = []
    if a:
        sum = 1
    for i in range(len(a)-1):
        if a[i]<=a[i+1]:
            sum +=1
        else:
            final_list_hours.append(sum)
            sum = 1
        final_list_hours.append(sum)
    print(final_list_hours)
    return max(final_list_hours)


print(studying_hours([2,2,9]))



