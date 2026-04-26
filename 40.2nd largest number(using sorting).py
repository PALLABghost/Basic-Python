
def second_largest(number):
    #as set dont allow any duplicate so all number is unique
    unique_number = list(set(number))

    # when length of the given input is too small
    if len(unique_number) < 2:
        return None      # program will not move
    #reverse shorting all the number
    unique_number.reverse()

    return unique_number[1]

nums = [24, 13 , 46 ,35 , 98 ,50 ,67 , 88 , 62 , 77 , 65, 24 , 46]
result = second_largest(nums)

if result is not None:
    print("second largets number is:", result)
else:
    print("list does not have enough unique number")






