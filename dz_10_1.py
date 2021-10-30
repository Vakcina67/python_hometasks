class Matrix:
    def __init__(self, m_1):
        self.m_1 = m_1

    def __str__(self):
        for row in self.m_1:
            for elem in row:
                print(elem, end=' ')
            print()
        return 'Матрица'

    def __add__(self, other):
        return Matrix([list(map(sum, zip(*i))) for i in zip(self.m_1, other.m_1)])



a = Matrix([[1, 2, 3], [3, -6, 8], [5, -55, 0]])
b = Matrix([[34, -43, 4], [9, -26, 0], [-5, 5, 40]])


print(a + b)