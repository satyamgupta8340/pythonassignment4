# 1. Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.¶

def sq():
    while True:
        try:
            a=int(input('Enter a number '))
            s=a**2
        except:
            print('Please Enter valid input ')
        else:
            print('The Square of a number is  ',s)
            break

sq()