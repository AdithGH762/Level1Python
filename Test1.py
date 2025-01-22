# def get_two_numbers(a,b):
#     return a,b
    
def add_two_numbers(a,b):
    return a+b

def show_results(a):
    return (f"sum is {a}")

def main():
    # a=int(input("Enter the number: "))
    # b=int(input("Enter the number: "))
    print(show_results(add_two_numbers(a=int(input("Enter the number: ")),b=int(input("Enter the number: ")))))
main()
