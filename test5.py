

# THIS IS USING DICTIONARY COMPREHENSION

def sanitize_input(input_string):
    key_value_pairs = input_string.split(";")

    for pair in key_value_pairs:
        if '=' in pair:
            key, value = pair.split("=",1)
            key = ''.join([char for char in key if char.isalnum()])
            value = ''.join([char for char in value if char.isalnum()])
            d = {key: value for key, value in zip(key, value)}
            # d[f'{key}'] = f'{value}'
    print(d)
user_input = "_syst*em=s;da(ta&base=d;us@er)name=u;pas]sword=p!"
ot = sanitize_input(user_input)
print("Sanitized Output:", ot)