
arr = [1,2,3,4,5]

def arr_rot(arr, n, rot):
    for i in range(rot):
        temp = arr[0]
        for i in range(0, n-1):
            arr[i] = arr[i+1]

        arr[n-1] = temp
        print(arr)

arr_rot(arr, 5, 1)
