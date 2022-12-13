# Question_1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below.

def hello_name(user_name):
    """Greet user by user name"""  
    user_name = input("Please type your user name.\n")
    print("hello_" + user_name.upper() + "!")

hello_name("")

# Question _2
#  Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing   
def first_odds():
    """Prints all odd numbers between 1 and 100 and return nothing"""
    for x in range(100):
        if x % 2 != 0:
            break
            print(x)            
first_odds()  

#  Question_3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    """Find the largest number in a list"""
    print(max(a_list))    

max_num_in_list(a_list)

#  Question_4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    """Check if a user inputted year is a leap year and return as boolean value"""
    a_year = input("Please enter a year.\n")
    a_year = int(a_year)
    return a_year % 4 == 0 and a_year % 100 != 0
         
print(is_leap_year(""))

#  Question_5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    """check if all numbers in a list are consecutive and return as boolean value"""
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
    
print(is_consecutive(a_list))

