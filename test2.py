# def main():
# a,b=input_two_numbers()
# sum=add(a,b)
# ouput(a,b,sum)
# main()
# input: 1 2
# output: 1+2 is 3

# Activity 3

def input_no():
    return int(input("Enter the Number: "))

def add(a,b):
    return a+b
def output(sum,a,b):
    print(f"The sum of {a} and {b} is {sum}")

def main():
    a=input_no()
    b=input_no()
    sum=add(a,b)
    output(sum,a,b)
main()