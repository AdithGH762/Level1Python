

# THIS IS USING DICTIONARY COMPREHENSION

def sanitize_input(input_string):
    d={}
    key_value_pairs = input_string.split(";")

    for pair in key_value_pairs:
        if '=' in pair:
            key, value = pair.split("=",1)
            key = ''.join([char for char in key if char.isalnum()])
            value = ''.join([char for char in value if char.isalnum()])
            d[f'{key}'] = f'{value}'
    return d
user_input = "_syst*em=s;da(ta&base=d;us@er)name=u;pas]sword=p!"
ot=sanitize_input(user_input)
print(ot)