#writing a recursive function to output every natural integer from 1-50 

n = 1

print( "the natural prder pf numbers from minimal to 50 is:" ) 

def print_to_fifty(n):
    print(n)
    if n == 50:
        return
    print_to_fifty( n + 1 )

print_to_fifty(n)
