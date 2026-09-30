def convert_10(string: str, n: int) -> int:
    num: int = 0
    try:
        for idx, i in enumerate(string):
            if not (int(i) < n):
                return -1 
            i = string[len(string) - 1 - idx]
            num += int(i) * n**idx
        return num
    except ValueError:
        return -1

def max_num(num: int, base: int):
    max_: int = 0
    index_tracker: int = 0
    while max_ < num:
        max_ += (base-1) * base**index_tracker
        index_tracker += 1
    return index_tracker

def convert_n(string: str, n: int, base: int) -> int:
    num = convert_10(string, n)
    new_string: int = -1
    if num != -1:
        new_string: str = ''
        index_tracker = max_num(num, base)
        while index_tracker > 0:
            possible_nums: list = []
            for i in range(base):
                if i * base ** (index_tracker - 1) <= num:
                    possible_nums.append(i)
            new_string += str(max(possible_nums))
            num -= max(possible_nums) * base ** (index_tracker - 1)
            index_tracker -= 1

    return int(new_string)        

def main():
    while True:
        string = input('Insert num: ')
        n = input('Insert base: ')
        new_base = input('Insert new base: ')
        try:
            n = int(n)
            new_base = int(new_base)
            print(convert_n(string, n, new_base))
        except ValueError:
            print(-1)

if __name__ == '__main__':
    main()
#add convert to other n base