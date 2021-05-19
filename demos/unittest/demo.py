class Operations:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_sum(self):
        z1 = (self.x + self.y)
        return z1

    def get_sub(self):
        z2 = (self.x - self.y)
        return z2

    def get_mult(self):
        z3 = (self.x * self.y)
        return z3

    def get_div(self):
        if self.y == 0:
            raise ValueError("0 is invalid for y")
        z4 = (self.x / self.y)
        return z4

    def get_double(self):
        z4 = self.x * 2
        return z4

    def get_square(self):
        z5 = self.x ** 2
        return z5

    def area_quadrado(self):
        area = self.x * self.x
        return area

    def area_retangulo(self):
        area_ret = self.x * self.y
        return area_ret


class Person:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_fullname(self):
        return '{} {}'.format(self.x, self.y)

    def get_email(self):
        return '{}.{}@email.com.br'.format(self.x, self.y).lower()
