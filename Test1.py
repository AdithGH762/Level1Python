def get_two_numbers(a,b):
    return a,b
    
def add_two_numbers(a,b):
    return a+b

def show_results(a,b):
    return (f"sum of {a} and {b} is {add_two_numbers(a,b)}")

def main():
    a=int(input("Enter the number: "))
    b=int(input("Enter the number: "))
    print(show_results(a,b))
main()
