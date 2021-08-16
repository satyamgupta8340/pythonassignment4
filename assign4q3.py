# 3. Write a Python program that accepts a string and calculate the number of digits and letters
#   Input :-Hello321Bye360
# .  Output:-Digit - 6,Letter - 8

s=input('Enter the string ')
d=0
l=0
for i in s:
    if i.isdigit():
        d=d+1
       
    elif i.isalpha():
        l=l+1
      
    else:
        pass
    
print(' Digit-',d)
print(' Letter-',l)