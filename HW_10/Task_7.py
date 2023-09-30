class Triangle:

    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @classmethod
    def check_sides(cls, side_a, side_b, side_c):
        if side_a >= side_b + side_c or side_b >= side_a + side_c or side_c >= side_b + side_a:
            return ('Треугольник не может существовать')

        else:
            if side_a == side_b == side_c:
                return ('Треугольник является равносторонним')
            elif side_a == side_b or side_a == side_c or side_b == side_c:
                return ('Треугольник является равнобедренным')
            else:
                return ('Треугольник является разносторонним')


print(Triangle.check_sides(3, 6, 8))
