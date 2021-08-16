# 4. You are given a string.Your task is to count the frequency of letters of the string and print the letters in descending order of frequency.
# for example :- If the following string is given as input to the program: aabbbccde
#   Then, the output of the program should be: b 3 a 2 c 2 d 1 e 1


word = input()
dct = {}
for i in word:
    dct[i] = dct.get(i,0) + 1

dct = sorted(dct.items(),key=lambda x:(-x[1],x[0]))
for i in dct:
    print(i[0],i[1],end=' ')