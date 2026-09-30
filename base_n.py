def convert_10(string: str, n: int) -> int:
    num = 0
    for idx, i in enumerate(string):
        i = string[len(string) - 1 - idx]
        num += int(i) * n**idx
        print(i)
    return num

print(convert_10('1111',2))