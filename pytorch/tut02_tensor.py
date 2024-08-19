# -*- coding: utf-8 -*-

import torch
import math


dtype = torch.float
device = torch.device("cpu")
# device = torch.device("cuda:0") # Uncomment this to run on GPU

# Create random input and output data
x = torch.linspace(-math.pi, math.pi, 2000, device=device, dtype=dtype)
y = torch.sin(x)

# Randomly initialize weights
a = torch.randn((), device=device, dtype=dtype)
b = torch.randn((), device=device, dtype=dtype)
c = torch.randn((), device=device, dtype=dtype)
d = torch.randn((), device=device, dtype=dtype)

learning_rate = 1e-6
for t in range(2000):
    # Forward pass: compute predicted y
    y_pred = a + b * x + c * x ** 2 + d * x ** 3

    # Compute and print loss
    loss = (y_pred - y).pow(2).sum().item()
    if t % 100 == 99:
        print(t, loss)

    # Backprop to compute gradients of a, b, c, d with respect to loss
    grad_y_pred = 2.0 * (y_pred - y)
    grad_a = grad_y_pred.sum()
    grad_b = (grad_y_pred * x).sum()
    grad_c = (grad_y_pred * x ** 2).sum()
    grad_d = (grad_y_pred * x ** 3).sum()

    # Update weights using gradient descent
    a -= learning_rate * grad_a
    b -= learning_rate * grad_b
    c -= learning_rate * grad_c
    d -= learning_rate * grad_d


print(f'Result: y = {a.item()} + {b.item()} x + {c.item()} x^2 + {d.item()} x^3')

"""
Result should look like this:

99 716.2569580078125
199 508.1888122558594
299 361.373779296875
399 257.75933837890625
499 184.6211700439453
599 132.98684692382812
699 96.52848815917969
799 70.78205871582031
899 52.597816467285156
999 39.75311279296875
1099 30.67894744873047
1199 24.267791748046875
1299 19.737659454345703
1399 16.536375045776367
1499 14.273929595947266
1599 12.674850463867188
1699 11.544556617736816
1799 10.745545387268066
1899 10.18069076538086
1999 9.781341552734375
Result: y = 0.03268956020474434 + 0.8536058068275452 x + -0.0056394897401332855 x^2 + -0.09288445860147476 x^3


"""