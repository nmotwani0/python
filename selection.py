def sort(nums):
    for i in range(len(nums)):
        minpos = i
        for j in range(i,len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j

        nums[i],nums[minpos] = nums[minpos],nums[i] 

        print(nums)



nums = [45,67,23,89,1,76,4]

print("Initial list",nums)

sort(nums)

print("Sorted List",nums)