import sys
import math


class SquareRoots:
    def __init__(self):
        self.coef_A = 0.0
        self.coef_B = 0.0
        self.coef_C = 0.0
        self.num_roots = 0
        self.roots_list = []

    def get_coef(self, index, prompt):
        try:
            coef_str = sys.argv[index]
        except:
            print(prompt)
            coef_str = input()
        coef = float(coef_str)
        return coef

    def get_coefs(self):
        self.coef_A = self.get_coef(1, 'Введите коэффициент А:')
        self.coef_B = self.get_coef(2, 'Введите коэффициент B:')
        self.coef_C = self.get_coef(3, 'Введите коэффициент C:')

    def calculate_roots(self):
        a = self.coef_A
        b = self.coef_B
        c = self.coef_C
        D = b * b - 4 * a * c
        if D == 0.0:
            root = -b / (2.0 * a)
            self.num_roots = 1
            self.roots_list.append(root)
        elif D > 0.0:
            sqD = math.sqrt(D)
            root1 = (-b + sqD) / (2.0 * a)
            root2 = (-b - sqD) / (2.0 * a)
            self.num_roots = 2
            self.roots_list.append(root1)
            self.roots_list.append(root2)

    def print_roots(self):
        if self.num_roots != len(self.roots_list):
            print(('Ошибка. Уравнение содержит {} действительных корней, ' +
                   'но было вычислено {} корней.').format(self.num_roots, len(self.roots_list)))
        else:
            if self.num_roots == 0:
                print('Нет корней')
            elif self.num_roots == 1:
                print('Один корень: {}'.format(self.roots_list[0]))
            elif self.num_roots == 2:
                print('Два корня: {} и {}'.format(self.roots_list[0],
                                                  self.roots_list[1]))


def main():
    r = SquareRoots()
    r.get_coefs()
    r.calculate_roots()
    r.print_roots()

if __name__ == "__main__":
    main()