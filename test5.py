# keys = ['a','b','c','d','e']
# values = [1,2,3,4,5]  

# def dict():
#     d={}
#     for i in keys:
#         for j in values:
            
# dict()


# myDict = { k:v for (k,v) in zip(keys, values)}  
# print (myDict)

def sanitize_input(input_string):
    key_value_pairs = input_string.split(";")
    d = {}

    for pair in key_value_pairs:
        if '=' in pair:
            key, value = pair.split("=",1)
            key = ''.join([char for char in key if char.isalnum()])
            value = ''.join([char for char in value if char.isalnum()])
            d[f'{key}'] = f'{value}'
    print(d)
user_input = "_syst*em=s;da(ta&base=d;us@er)name=u;pas]sword=p!"
ot = sanitize_input(user_input)
