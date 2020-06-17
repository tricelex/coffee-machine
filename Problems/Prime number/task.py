# num = int(input())
#
# if num > 1:
#     if num % 2 == 1:
#         print('This number is prime')
#     else:
#         print('This number is not prime')
# else:
#     print('This number is not prime')
#
#


# Program to check if a number is prime or not

num = int(input())

# To take input from the user
# num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print('This number is not prime')
            break
    else:
        print('This number is prime')

# if input number is less than
# or equal to 1, it is not prime
else:
    print('This number is not prime')
