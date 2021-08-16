#5. You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:¶
 #      Sort based on name
  #    Then sort based on age
   #   Then sort by score
   #   The priority is that name > age > score.
 #     If the following tuples are given as input to the program:
 #     Tom,19,80
 #    John,20,90
 #     Jony,17,91
 #     Json,21,85
  #    Then, the output of the program should be:
  #     [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

from operator import itemgetter

people_info = []
while True:
    individual_info = input()

    if individual_info == "":
        break
    else:
        people_info.append(tuple((individual_info.split(","))))

people_info.sort(key =  itemgetter(0, 1, 2))       
print(people_info)