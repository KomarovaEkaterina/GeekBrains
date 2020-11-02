import re


class ComplexNumber:
    def __init__(self, num):
        self.num = num

    @staticmethod
    def get_num(nm):
        x = [int(el) for el in re.findall(r'\d+', nm.replace(' ', ''))][0]
        y = [int(el) for el in re.findall(r'.\d+', nm.replace(' ', ''))][0]
        return x, y

    def __add__(self, other):
        x1, y1 = self.get_num(self.num)
        x2, y2 = self.get_num(other.num)
        res_f = x1 + x2
        res_s = y1 + y2
        if res_s < 0:
            res = f"{res_f}{res_s}j"
        else:
            res = f"{res_f}+{res_s}j"
        return ComplexNumber(res)

    def __mul__(self, other):
        x1, y1 = self.get_num(self.num)
        x2, y2 = self.get_num(other.num)
        res_first = (x1 * x2 - y1 * y2)
        res_sec = (x1 * y2 + x2 * y1)
        if res_sec < 0:
            res = f"{res_first}{res_sec}j"
        else:
            res = f"{res_first}+{res_sec}j"
        return ComplexNumber(res)


a = ComplexNumber("2-3j")
b = ComplexNumber("3+1j")
c = ComplexNumber("2+1j")
d = ComplexNumber("3+5j")
print(f"{c.num} + {d.num} = {(c + d).num}")
print(f"{a.num} * {b.num} = {(a * b).num}")
