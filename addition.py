sum = 0
listofnumbers = []
while sum < 100:
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        num = int(user_input)
        if num > 100:
            print("entered number is greter than 100.")
        else:
            listofnumbers.append(num)
            sum += num
            print("Current sum: ", sum)
    else:
        print("enter only integer.")
print("sum 100 is completed.")
print("entered numbers list ", listofnumbers)