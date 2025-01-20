def get_two_numbers(a,b):
    return a,b
    
def add_two_numbers(a,b):
    a,b=get_two_numbers(a,b)
    return a+b

def show_results(a,b):
    return (f"sum of {a} and {b} is {add_two_numbers(a,b)}")

a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
print(show_results(a,b))