import numpy as np
from hw8.task1 import task1
from hw8.task2 import task2

__author__ = 'KatyaKos'

print('Enter number of task: 1-2')
task = int(input())
print('Enter number of iterations:')
steps = int(input())
x0 = 1.0
y0 = 1.0
if task == 1:
    l = 1.0
    L = 69.0

    print('Heavy ball method:')
    xy, f = task1(0, steps, x0, y0, l, L)
    print('x1 =', xy[0], '\nx2 =', xy[1], '\nf_value =', f, sep=' ')

    print('\nNesterov method:')
    x, y, f = task1(1, steps, x0, y0, l, L)
    print('x =', x, '\ny =', y, '\nf_value =', f, sep=' ')

    print('\nChebushev method:')
    xy, f = task1(2, steps, x0, y0, l, L)
    print('x1 =', xy[0], '\nx2 =', xy[1], '\nf_value =', f, sep=' ')
else:
    l = 0.0
    L = 0.0

    print('\nNesterov method:')
    (x, y, f), realf = task2(steps, x0, y0, l, L)
    print('x =', x, '\ny =', y, '\nf_value =', f, sep=' ')
    print('Delta between real minimum and the one we found: ', f - realf)
