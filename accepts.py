import math

def accepts(*arg_types):
    def arg_check(func):
        def new_func(*args):
            for arg, arg_type in zip(args,arg_types):
                if type(arg) != arg_type:
                    print "Argument", arg, "is not of type", arg_type
                    break
            else:
                func(*args)
        return new_func
    return arg_check


@accepts(complex)
def complex_magnitude(z):
    print math.sqrt(z.real**2 + z.imag**2)

@accepts(str)
def print_greeting(name):
    print "Hello, " + name.capitalize()

@accepts(dict, int)
def avg_temps(records, year):
    for month, temp in records.items():
        print "The average temperature in", month, year, "was", temp, "F."


if __name__ == "__main__":
    complex_magnitude("hello")
    complex_magnitude(1+1j)

    print_greeting(1+2)
    print_greeting("ben")

    avg_temps([("January", 58.2), ("February", 60.1)], "2016")
    avg_temps({"January": 58.2, "February": 60.1}, 2016)
