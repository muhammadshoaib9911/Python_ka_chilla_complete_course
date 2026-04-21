# Logicals operators are either "True or False" "OR" "yes or no" or "1 or 0"
# Greater than     : >
# Less than        : <  
# Greater or equal : >=
# Less or equal    : <=
# Equal to         : ==
# Not equal to     : !=
# And operator     : and
# Or operator      : or

# is 5 equal to 5?
print(5 == 5)  #True
print(5 != 5) #False
print(5 > 3) #True
print(5 < 3) #False
print(5 >= 5) #True    
print(5 <= 3) #False
print(5 <= 5) #True
print(3 <= 5) #True
print(3 >= 5) #False

#Applications of logical opperators
hammad_age = 4
age_at_school = 5
print(hammad_age >= age_at_school) #False
print(hammad_age < age_at_school)  #True

#input function and logical operators
age_at_school = 5
hammad_age = int(input("How old is Hammad? ")) #input function always returns string so we need to convert it to integer using int()
print(age_at_school == hammad_age) #logical operator to check if Hammad is of school age
