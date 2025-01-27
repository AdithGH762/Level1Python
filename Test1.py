def main():
    def add(a,b):
        return a+b

    def output(a):
        return ("sum is {}".format(a))
    print(output(add(a=int(input("Enter the number: ")),b=int(input("Enter the number: ")))))
main()