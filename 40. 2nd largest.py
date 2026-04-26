def second_largest(number):
    if len(number) < 2:
        return None

    largest = second = float("-inf") #negative infinite

    for num in number:
        if num > largest:
            # Update both largest and second largest
            second = largest
            largest = num
        elif num > second and num != largest:
            # Update second largest only if any other num exist between large and second, then the number = second
            second = num
    return second if second != float('-inf') else None

nums = [24, 13 , 46 ,35 , 98 ,50 ,67 , 88 , 62 , 77 , 65, 24 , 46]
result = second_largest(nums)

if result is not None:
    print("Second largest number is:", result)
else:
    print("List does not have enough unique numbers.")
