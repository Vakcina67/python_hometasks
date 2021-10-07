from random import choice

def get_jokes(n, arg=True):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    i = 0
    if n > min(len(nouns), len(adverbs), len(adjectives)):
        n = min(len(nouns), len(adverbs), len(adjectives))
    while i < n:
        a = choice(nouns)
        b = choice(adverbs)
        c = choice(adjectives)
        jokes.append(f'{a} {b} {c}')
        if arg == True:
            nouns.remove(a)
            adverbs.remove(b)
            adjectives.remove(c)
        i += 1
    return jokes

print(get_jokes(4))
print(get_jokes(4, False))

