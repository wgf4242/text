def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10


def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0


if __name__ == '__main__':
    f = open('result/IMEI校验位.txt', 'r').read().splitlines()
    res = open('imei.txt', 'w')
    for line in f:
        fl = is_luhn_valid(int(line))
        is_luhn_valid(4532015112830366)
        print(fl)
        if fl:
            res.write(line+'\n')
    # result = is_luhn_valid(4532015112830366)
    # print('Correct:' + str(result))
    # result = is_luhn_valid(6011514433546201)
    # print('Correct:' + str(result))
    # result = is_luhn_valid(6771549495586802)
    # print('Correct:' + str(result))
