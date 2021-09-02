user_sec = int(input('Введите колличество секунд: '))

#  не уверен что использование словаря в данном случае актуально, но лучше на данный момент не придумал
unit = {
    'minute': 60,
    'hour': 3600,
    'day': 86400
}


#  Можно сделать return в одну строку, но будет совсем не читаемо. Конечно, если не использвать импорты.
def get_time_distance(seconds):
    day = seconds // unit['day']
    hour = (seconds % unit['day']) // unit['hour']
    minutes = ((seconds % unit['day']) % unit['hour']) // unit['minute']
    sec = ((seconds % unit['day']) % unit['hour']) % unit['minute']
    if not day:
        if not hour:
            if not minutes:
                return f"{sec} сек"
            return f"{minutes} мин {sec} сек"
        return f"{hour} час {minutes} мин {sec} сек"
    return f"{day} дн {hour} час {minutes} мин {sec} сек"


if __name__ == '__main__':
    print(get_time_distance(user_sec))

# Если без функции - то вот мастхэв мануал =)
# if seconds < unit['minute']:
#     print(f'{seconds} сек')
# elif unit['minute'] < seconds < unit['hour']:
#     minutes = seconds // unit['minute']
#     sec = seconds % unit['minute']
#     print(f"{minutes} мин {sec} сек")
# elif unit['hour'] < seconds < unit['day']:
#     hour = seconds // unit['hour']
#     minutes = (seconds % unit['hour']) // unit['minute']
#     sec = (seconds % unit['hour']) % unit['minute']
#     print(f'{hour} час {minutes} мин {sec} сек')
# else:
#     day = seconds // unit['day']
#     hour = (seconds % unit['day']) // unit['hour']
#     minutes = ((seconds % unit['day']) % unit['hour']) // unit['minute']
#     sec = ((seconds % unit['day']) % unit['hour']) % unit['minute']
#     print(f"{day} дн {hour} час {minutes} мин {sec} сек")
