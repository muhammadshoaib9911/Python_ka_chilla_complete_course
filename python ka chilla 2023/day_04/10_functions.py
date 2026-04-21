#function 1
def print_codenics():
    print("Codenics")
    print("Codenics")
    print("Codenics")
    print("Codenics")
print_codenics()

#function 2
def print_codenics():
    text = "Codenics"
    print(text)
    print(text)
    print(text)
print_codenics()

#function 3
def print_codenics(text):
    print(text)
    print(text)
    print(text)
print_codenics("Hello Codenics")

#function 4 
# definining a function with if else and elif statements
def school_calculator(age):
    if age == 5:
        print("Ali can go to school")
    elif age > 5:
        print("Ali should be in higher class")
    else:
        print("Ali is too small to go to school")
        
school_calculator(4) #Ali is too small to go to school


#future age calculator function
def future_age(age):
    new_age = age + 5
    return new_age
print(future_age(10))  #15

future_predicted_age = future_age(20)
print(future_predicted_age)  #25