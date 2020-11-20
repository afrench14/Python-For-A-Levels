#writing a recursive function to output every natural integer from 1-50 

n = 5
print( "the addition pog numbers from 1 to " + n + " is: " ) 

def add_to_n(n):
    overall_value = 0
    overall_value += n
    if n == 0:
        return
    add_to_n( n - 1 )

total = add_to_n(n)
print(total)
