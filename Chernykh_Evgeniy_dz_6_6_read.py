import sys

if __name__ == '__main__':
    num_price = list(map(int, sys.argv[1:]))
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        text = f.readlines()
        if len(num_price) == 2:
            for line in text[num_price[0] - 1:num_price[1]]:
                print(line.strip())
        elif len(num_price) == 1:
            for line in text[num_price[0] - 1:]:
                print(line.strip())
        else:
            for line in text:
                print(line.strip())
    exit()