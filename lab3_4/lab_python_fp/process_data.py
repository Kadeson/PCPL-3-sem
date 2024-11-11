import json
from lab_python_fp.gen_random import gen_random
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1

path = 'E:/Study/projects/lab3_4/lab_python_fp/data_light.json'

with open(path) as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(set(job['job-name'].lower() for job in arg), key=lambda x: x.lower())


@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: f"{x} с опытом Python", arg))


@print_result
def f4(arg):
    return [f"{x}, зарплата {next(gen_random(1, 100000, 200000))} руб." for x in arg]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
