arr = [1, 2, 3, 4, 5]
k = 2  # number of right rotations

n = len(arr)
for _ in range(k):
    last = arr[n-1]
    # shift everything one step to right
    for i in range(n-2, -1, -1):
        arr[i+1] = arr[i]
    arr[0] = last

print("After Right Rotation:", arr)
# Output: [4, 5, 1, 2, 3]
