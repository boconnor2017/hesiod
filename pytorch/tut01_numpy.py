# -*- coding: utf-8 -*-
import numpy as np
import math

# Create random input and output data
x = np.linspace(-math.pi, math.pi, 2000)
y = np.sin(x)

# Randomly initialize weights
a = np.random.randn()
b = np.random.randn()
c = np.random.randn()
d = np.random.randn()

learning_rate = 1e-6
for t in range(2000):
    # Forward pass: compute predicted y
    # y = a + b x + c x^2 + d x^3
    y_pred = a + b * x + c * x ** 2 + d * x ** 3

    # Compute and print loss
    loss = np.square(y_pred - y).sum()
    if t % 100 == 99:
        print(t, loss)

    # Backprop to compute gradients of a, b, c, d with respect to loss
    grad_y_pred = 2.0 * (y_pred - y)
    grad_a = grad_y_pred.sum()
    grad_b = (grad_y_pred * x).sum()
    grad_c = (grad_y_pred * x ** 2).sum()
    grad_d = (grad_y_pred * x ** 3).sum()

    # Update weights
    a -= learning_rate * grad_a
    b -= learning_rate * grad_b
    c -= learning_rate * grad_c
    d -= learning_rate * grad_d

print(f'Result: y = {a} + {b} x + {c} x^2 + {d} x^3')

"""
Output should look like this:

99 48.13028639429092
199 35.342154156065945
299 26.7359809713862
399 20.93430089135758
499 17.01949793813467
599 14.37532473505382
699 12.587583534627335
799 11.377641850809171
899 10.557896686396578
999 10.001919779624929
1099 9.624429213949274
1199 9.367842595033398
1299 9.193241650149973
1399 9.074295887675742
1499 8.993172661456999
1599 8.937781781351529
1699 8.899917478585422
1799 8.874004281214098
1899 8.856249679722502
1999 8.844071057864873
Result: y = 0.004258017812573502 + 0.8599240780420037 x + -0.0007345789263911657 x^2 + -0.09378317649497404 x^3


"""