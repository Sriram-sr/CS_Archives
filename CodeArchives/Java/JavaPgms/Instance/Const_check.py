class Check:
    int_var = 9
    str_var = "Class variable"

    def __init__(self):
        print(Check.int_var,Check.str_var)

obj = Check()        