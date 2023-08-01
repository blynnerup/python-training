def max_magnitude(ls):
    return max(abs(num) for num in ls)

print(max_magnitude([1,2,3,-88]))

def sum_even_values(*args):
    return sum([num for num in args if num % 2==0])

print(sum_even_values(1,2,3,4,6))

def sum_floats(*args):
    return sum([num for num in args if isinstance(num, float)])

print(sum_floats(1,2,3.5,6,7.5))
