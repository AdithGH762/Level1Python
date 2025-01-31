def sanitize_input(input_string):
    d={}
    key_value_pairs = input_string.split(";")

    for pair in key_value_pairs:
        if '=' in pair:
            key, value = pair.split("=",1)
            if not key.isalnum() and not value.isalnum():
                print(f"Invalid KEY: {key} and VALUE: {value}") 
            elif not key.isalnum():
                print(f"Invalid key: {key}")
            elif not value.isalnum():
                print(f"Invalid value: {value}")
            else:
                d[key] = value
    return d
user_input = "system=s;dat#abase=+)d;user=name;password=)p;environment=pro*d"
print(sanitize_input(user_input))