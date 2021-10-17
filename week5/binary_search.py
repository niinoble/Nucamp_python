def binary_search(the_list, target):
    lower_bound = 0
    uppper_bound = len(the_list) -1
    
    while lower_bound <= uppper_bound:
        pivot = (lower_bound + uppper_bound) //2
        pivot_value = the_list[pivot]

        if pivot_value == target:
            return pivot
        if pivot_value > target:
            uppper_bound = pivot - 1
        else: 
            lower_bound = pivot + 1

    return -1

my_list = [1,2,3,4,5,6,7,8,9,10,12]

print(binary_search(my_list,10))
print(binary_search(my_list,4))
print(binary_search(my_list,33))