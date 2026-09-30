def convert_10(string: str, n: int) -> int:
    num = 0
    try:
        for idx, i in enumerate(string):
            if not (int(i) < n):
                return -1 
            i = string[len(string) - 1 - idx]
            num += int(i) * n**idx
        return num
    except ValueError:
        return -1

while True:
    string = input('Insert num: ')
    try:
        n = int(input('Insert base: '))
        print(convert_10(string, n))
    except ValueError:
        print(-1)