
def double(a=[0,2,5,4,1,0,3,3,6,7]):
    temp_list0 = []
    temp_list = []
    for i,j in enumerate(a):
        try:
            if a[i] == a[i+1]:
                a[i+1] = 0
                a[i] = a[i]*2
            else:
                a[i] = a[i]*2

        except IndexError:
            a[i] = a[i]*2
            break

    for i in a:

        if i == 0:
            temp_list0.append(i)
        else:
            temp_list.append(i)
    temp_list0.extend(temp_list)

    return temp_list0


print(double())
    





