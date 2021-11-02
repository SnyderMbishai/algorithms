def change_to_zero(arr):
    # arr_c = arr
    cols = []
    rows = []
    l_rows = len(arr)
    for i,a in enumerate(arr):
        for ii,j in enumerate(a):
            if j == 0:
                rows.append(i)
                cols.append(ii)
    for i in rows:
        arr[i] = [0,0,0,0]
    for i in cols:
        for a in range(l_rows):
            arr[a][i] = 0
    print(arr)



arr = [
    [5,4,3,9],
    [2,0,7,6],
    [1,3,4,0],
    [9,8,3,4]
]

change_to_zero(arr)