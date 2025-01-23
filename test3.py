# def main():
# cs=get_cs()
# lot=cs_to_lot(cs) # convert connect string to list of tuples
# print(lot)
# main()
# ______________________________________________________________________________________
# Input:
# system=s;database=d;username=u;password=p

# Output:
# [('system','s'),(database','d'),('username','u'),('password','p')]

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

# def get_cs():
#     return input("Enter the connecting string : ")
# def cs_to_lot(cs):
#     lot=[]
#     pairs=cs.split(";")
#     for pair in pairs:
#         key,value=pair.split("=")
#         lot.append((key,value))
#     return lot
# def main():
#     cs=get_cs()
#     result=cs_to_lot(cs)
#     print(result)
# print(main())

# -------------------------------------------------------------------------------------

# using list comprehension method

def get_cs():
    return input("Enter the connecting string : ")
def cs_to_lot(cs):
    return [tuple(pair.split("=")) for pair in cs.split(";")]
def main():
    print(cs_to_lot(get_cs()))
main()