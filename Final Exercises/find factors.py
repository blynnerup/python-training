def find_factors(input_num):
    factor_list = [num for num in range(1, input_num+1) if input_num % num == 0] 
    return factor_list

print(find_factors(10))
print(find_factors(11))
print(find_factors(111))
print(find_factors(321421))