# def main():
# a,b=input_two_numbers()
# sum=add(a,b)
# ouput(a,b,sum)
# main()
# input: 1 2
# output: 1+2 is 3

# Activity 3

def input_no():
    a = int(input("Enter the Number: "))
    b = int(input("Enter the Number: "))
    return a,b

def add():
    a,b=input_no()
    return a+b

def output():
    sum=add()
    print(f"The sum is {sum}")

def main():
    output()
main()