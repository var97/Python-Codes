
arr = [1,2,3,4,5]

def arr_rot(arr, n, rot):
    for i in range(rot):
        temp = arr[n-1] 
        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1]

        arr[0] = temp
        print(arr)

arr_rot(arr, 5, 1)
