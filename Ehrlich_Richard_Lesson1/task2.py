odd_numbers_list = [num ** 3 for num in range(1, 1000, 2)]


#  section A
def get_sum_numbers_multiples_of_seven(list_num):
    total = 0
    result = 0
    for number in list_num:
        tmp = number
        while tmp:
            total += tmp % 10
            tmp = tmp // 10
        if total % 7 == 0:
            result += number
        total = 0
    return result


print(get_sum_numbers_multiples_of_seven(odd_numbers_list))

#  section B
print(get_sum_numbers_multiples_of_seven([item + 17 for item in odd_numbers_list]))

#  section C
for index in range(len(odd_numbers_list)):
    odd_numbers_list[index] = odd_numbers_list[index] + 17
print(get_sum_numbers_multiples_of_seven(odd_numbers_list))