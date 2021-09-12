import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(lot, *args, flag=False):
    list_jokes = []
    while lot:
        joke = list(map(random.choice, args))
        if flag and len(list_jokes) > 0:
            if lot <= len(min(args)):
                for phrase in list_jokes:
                    for word in joke:
                        if word in phrase:
                            flag = False
                            continue
                if flag:
                    list_jokes.append(joke)
                    lot -= 1
                flag = True
            else:
                return ["Запрос уникальных шуток превышает возможности выдачи."]
        else:
            list_jokes.append(joke)
            lot -= 1
    return list_jokes


if __name__ == '__main__':
    try:
        print(*get_jokes(5, nouns, adverbs, adjectives, flag=True), sep='\n')
        # Уникальность выдачи регулируется присутствием именованного аргумента flag
    except Exception:
        print("Введено не корректное значение")
