import math


class BSS:
    p = 87566873
    q = 15485143
    s = 740191
    M = p * q
    seed = s
    count = 0

    def gcd(self, a, b):
        if (b == 0):
            return a
        else:
            return self.gcd(b, math.fmod(a, b))

    def get_rand(self):
        self.count += 1
        g = self.gcd(self.p, self.q)
        lcm = self.p * self.q / g
        exp = 1
        for j in range(1, self.count + 1):
            exp = math.fmod((exp + exp), lcm)
        x = self.seed * self.seed
        r = x

        for j in range(2, int(exp + 1)):
            r = math.fmod((r * x), self.M)

        return r


bss = BSS()


def show_me_the_hand(records):
    ans = int(math.fmod(bss.get_rand(), 3))
    if (ans == 0):
        ans = 'gawi'
    elif (ans == 1):
        ans = 'bawi'
    else:
        ans = 'bo'
    return ans