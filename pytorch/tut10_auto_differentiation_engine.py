import torch

"""
Automatic Differentiation is a set of techniques to evaluate the partial derivative of a function
    specified by a computer program.

Partial derivative of a function of several variables is its derivative with respect to one
    of those variables, with others held constant. These are critical for adjusting the
    weights of a neural network during training. The weights determine how much each input
    factor (i.e. tensor) contributes to the final prediction. During the training process
    the neural network makes predictions based on the current weights. These predictions
    are compared to the actual target values and an error is calculated. To minimize this error
    the weights need to be adjusted. The derivative tells us how the error changes when a 
    weight is adjusted. Partial derivatives are used when there are multiple weights to adjust. 
    They tell us how the error changes when we tweak just one weight while keeping the others fixed.
    By adjusting each weight in the direction indicated by its partial derivative, we can 
    gradually improve the neural network's predictions and minimize the overall error. 

torch.

    randn(size): returns a tensor filled with random numbers froma  normal distribution
    with mean 0 and variance 1. https://pytorch.org/docs/stable/generated/torch.randn.html 

    mm(input, mat2): performs matrix multiplication of the matrices input and mat2.
        input = the first tensor
        mat2 = a second tensor

    t(input): expects input to be less than or equal to a 2-D tensor and transposes dimensions 0 and 1.
        * Transpose: to reverse or transfer to order or place of; interchange. 
        When the input is a 2-D tensor this is equivalent to `transpose(input, 0, 1)`

    transpose(input, dim0, dim1): returns a tensor that is a transposed version of input. The
        given dimensions dim0 and dim1 are swapped.
"""

x = torch.randn(1, 10)
prev_h = torch.randn(1, 20)
W_h = torch.randn(20, 20)
W_x = torch.randn(20, 10)

i2h = torch.mm(W_x, x.t())
h2h = torch.mm(W_h, prev_h.t())
next_h = i2h + h2h 
next_h = next_h.tanh()

loss = next_h.sum()
#loss.backward()