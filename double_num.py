def main():
    nums = [2, 7, 11, 15]
    target = 9
    n = len(nums)

    dictionary = {}

    for i in range(n):
        match = target - nums[i]
        try:
            print(i, nums.index(match))
            break
        except ValueError:
            pass


    print("hello")


main()

