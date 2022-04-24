def get_next_big_num(list_num):
    tmp_list = []
    previous_number = 0
    for item in list_num:
        if previous_number and previous_number < item:
            tmp_list.append(item)
            previous_number = item
        else:
            previous_number = item
    return tmp_list


def get_next_big_num_new(list_num):
    previous_number = 0
    for item in list_num:
        if previous_number and previous_number < item:
            previous_number = item
            yield item
        else:
            previous_number = item


if __name__ == '__main__':
    from sys import getsizeof
    from timeit import Timer

    src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    # Timer нашёл в сети. Как он работает пока не понимаю.

    print(*get_next_big_num(src), 'size: ->', getsizeof(get_next_big_num(src)), 'timer: ->',
          Timer("get_next_big_num(src)", globals=globals()).timeit(),
          type(get_next_big_num(src)))
    # 12 44 4 10 78 123 size: -> 120 timer: от  -> 2.000000000002e-06  до   -> 4.199999999995874e-06
    # <class 'list'>

    print(*get_next_big_num_new(src), 'size: ->', getsizeof(get_next_big_num_new(src)), 'timer: ->',
          Timer("get_next_big_num(src)", globals=globals()).timeit(),
          type(get_next_big_num_new(src)))
    # 12 44 4 10 78 123 size: -> 112  timer: от  -> 2.2000000000008124e-06  до   -> 4.4999999999975615e-06
    # <class 'generator'>

    # Однострочное решение
    one_line_result = (src[index + 1] for index in range(len(src) - 1) if src[index + 1] > src[index])

    print(*one_line_result, 'size: ->', getsizeof(one_line_result), 'timer: ->',
          Timer("get_next_big_num(src)", globals=globals()).timeit(), type(one_line_result))
    # 12 44 4 10 78 123 size: -> 112   timer: от  -> 2.3999999999996247e-06  до   -> 4.200000000002813e-06
    # <class 'generator'>
# После твоего совета в комментариях на GITHUB поменял код таймера и ДА) разниза очевидно заметна:)
# 12 44 4 10 78 123 size: -> 120 timer: -> 2.5153080300005968 <class 'list'>
# 12 44 4 10 78 123 size: -> 112 timer: -> 1.9824268449992815 <class 'generator'>
# 12 44 4 10 78 123 size: -> 112 timer: -> 1.9674390750005841 <class 'generator'>
