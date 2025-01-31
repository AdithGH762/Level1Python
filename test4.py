# def main():
# cs=get_cs()
# lot=cs_to_lot(cs) # convert connect string to list of tuples
# print(lot)
# cs=lot_to_cs(lot)
# print(cs)
# main()
# ------------------------------------------------------------------------------------------------
# Input:
# system=s;database=d;username=u;pas]sword=p

# Output:
# [('system','s'),('database','d'),('username','u'),('passwd','p')]
# system=s;database=d;username=u;password=p


def sanitize_input(input_string):
    sanitized_pairs = []
    key_value_pairs = input_string.split(";")

    for pair in key_value_pairs:
        if '=' in pair:
            key, value = pair.split("=",1)
            print(key, value)
            sanitized_key = ''.join([char for char in key if char.isalnum()])
            sanitized_value = ''.join([char for char in value if char.isalnum()])
            sanitized_pairs.append(sanitized_key + "=" + sanitized_value)

    return ";".join(sanitized_pairs)

user_input = "`sy~s         ~te@!m=     s;da%$#tab^ase=#$%d   ;us=e=r(na)me=u;pas]sword=p;env$ironment=prod@#;"
ot = sanitize_input(user_input)
print("Sanitized Output:", ot)

def cs_to_lot(cs):
    return [tuple(pair.split("=")) for pair in cs.split(";")]
def main():
    print(cs_to_lot(ot))
main()