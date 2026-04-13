doubles = [x *2 for x in range(1,10)]
print(doubles)

sqare = [pow(y,2) for y in range(1,6)]
print(sqare)
fruits = ["apple", "banana", "orange"]
fruit_char = [z[0] for z in fruits]
print(fruit_char)

number =  [1, -2, 3, -4 , 5, -6 ,8]
pos_num= [num for num in number if num >= 0]
print(pos_num)

#eve_num = [num for num in number if num%2==0]
eve_num = [num for num in number if (int(num/2))*2==num]
odd_num = [num for num in number if num%2!=0]
print(eve_num)
print(odd_num)



