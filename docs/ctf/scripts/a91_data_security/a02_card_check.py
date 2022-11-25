### 银行卡号校验 Luhn算法
def cardCheck(s):
    def f(i, c):
        if i % 2 == 0: return c
        t = c * 2
        if t > 9: t -= 9
        return t

    lst = [f(i, int(c)) for i, c in enumerate(reversed(s))]
    return sum(lst) % 10 == 0


if __name__ == '__main__':
    f = open('out/BankCard.txt', 'r').read().splitlines()
    res = open('final/BankCard.txt', 'w')
    for line in f:
        a,b,line = line.split(',')
        fl = cardCheck(line)
        if fl:
            res.write(','.join([a,b,line])+'\n')
    # print(cardCheck('6225760008219525'))
