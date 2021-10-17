import sys

if __name__ == '__main__':
    price = sys.argv[1]
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(price + '\n')
    exit()