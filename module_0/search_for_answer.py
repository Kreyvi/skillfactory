def search_number(search, low, high, counter=0):
    counter += 1
    mid = (low + high) // 2
    if search == mid:
        return counter
    if search > mid:
        return search_number(search, mid + 1, high, counter)
    if search < mid:
        return search_number(search, low, mid, counter)


if __name__ == '__main__':
    import random as rnd

    num = rnd.randint(0, 100)
    try_counts = search_number(num, 0, 100)
    print(f'Загаданное число: {num}')
    print(f'Найдено за {try_counts} попыток')
