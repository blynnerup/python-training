def remove_every_other(input_list):
    reduced_list = input_list[::2]
    return reduced_list

print(remove_every_other([1,2,3,4,5]))
print(remove_every_other([5,1,2,4,1]))
print(remove_every_other([1]))