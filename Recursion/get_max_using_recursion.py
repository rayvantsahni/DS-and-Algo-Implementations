def get_max_using_recursion(arr):
    if not arr:
        print("-- No Item in List --")
        return float('inf')
    if len(arr) == 1:
        return arr[0]
    return max(arr[0], get_max_using_recursion(arr[1:]))




if __name__ == "__main__":
    arr = [8,6,3,1,5,10,7,3]
    # arr=[]
    print(f"Max: {get_max_using_recursion(arr)}")