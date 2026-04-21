x = 10  #integer
y = 3.5 #float  
z = 'Hello' #string

#implicit type conversion
a = x + y  #integer + float = float
print(a)  #13.5
print(type(a))  #<class 'float'>
b = x * 2  #integer * integer = integer
print(b)  #20
print(type(b))  #<class 'int'>

#explicit type conversion
age = input ("Enter your age: ")  #input function returns string
age = int(age)  #convert string to integer 
print(type(int(age)))  #<class 'str'> 

print(age, type(float(age)))  #prints age and its type after converting to float

#convert integer to string
age_str = str(age)
print(age_str, type(age_str))  #prints age and its type after converting to string


