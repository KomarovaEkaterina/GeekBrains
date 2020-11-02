class MyClass:
    def __init__(self, p_1):
        self.p_1 = p_1

    def __add__(self, other):
        mtx = []
        while True:
            if len(self.p_1) > len(other.p_1):
                other.p_1.append([0])
            elif len(self.p_1) < len(other.p_1):
                self.p_1.append([0])
            else:
                break
        for i in range(len(self.p_1)):
            while True:
                if len(self.p_1[i]) > len(other.p_1[i]):
                    other.p_1[i].append(0)
                elif len(self.p_1[i]) < len(other.p_1[i]):
                    self.p_1[i].append(0)
                else:
                    break
            ln = []
            for j in range(len(self.p_1[i])):
                ln.append(self.p_1[i][j] + other.p_1[i][j])
            mtx.append(ln)
        return MyClass(mtx)

    def __str__(self):
        st = ''
        for i in range(len(self.p_1)):
            for j in range(len(self.p_1[i])):
                st += f"{self.p_1[i][j]:3}" + ' '
            st += '\n'
        return st[:-1]


a = [[5, 4, 2, 6], [34, 9, 3]]
b = [[1, 6, 5, 18], [1, 3], [0, 9, 3, 2], [8, 7, 3, 2]]
c = [[1, 10, 15, 3], [11, 2, 10, 1], [4, 3, 2, 50]]
my_1 = MyClass(a)
my_2 = MyClass(b)
my_3 = MyClass(c)
print(my_1 + my_2 + my_3)
