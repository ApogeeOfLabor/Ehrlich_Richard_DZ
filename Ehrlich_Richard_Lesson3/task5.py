import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(lot, *args, flag=False):
    list_jokes = []
    for n in range(lot):
        joke = list(map(random.choice, args))
        if flag and len(list_jokes) > 0:
            for phrase in list_jokes:
                for word in joke:
                    if word not in phrase and phrase == list_jokes[-1]:
                        list_jokes.append(joke)
                        # пока не работает
        else:
            list_jokes.append(joke)
    return list_jokes


if __name__ == '__main__':
    print(*get_jokes(len(nouns), nouns, adverbs, adjectives, flag=True))
