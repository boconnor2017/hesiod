import numpy as np
import pandas as pd
import torch
import torch.optim as optim
import torch.nn as nn
from torch.autograd import Variable

# numpy.random module implements pseudo random number generators
# random.seed module sets the random seed to a certain value
np.random.seed(68)  # random seed = 68

# torch.manual_seed sets the seed for generating random numbers on all devices
torch.manual_seed(0) # random seed = 0

# Ensures the model and the data are on the same device
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

"""
Floating point numbers have a wide range of values.
They require less memory.
They are easy to perform complex computations. 
A numpy array with dtype float-32 and float-64 occupies 4 bytes and 8 bytes respectively in memory.
"""

# Preserves memory
torch.set_default_tensor_type(torch.FloatTensor)

# Inputs to the neural network (x)
# numpy.array creates an array (a vector)
t_c = [1.0]
t_u = [1.0]
t_c = np.array(t_c)
t_u = np.array(t_u)

"""
torch.autograd() i.e. Variable() provides classes and functions implementing automatic 
differentiation of arbitrary scalar valued functions. You need to declare Tensors for 
which gradients should be computed with the `requires_grad=True` keyword.

This method only supports autograd for floating point Tensor types.
(r) in this context is the data point converted to floating point Tensor.  

to(device) simply ensures the model and the data are on the same device. Data running
on CPU and model running on GPU (or vice-versa) will result in runtime error. 
"""

def numpy_to_variable(r):
    return Variable(torch.from_numpy(r).float(), requires_grad=True).to(device)

"""
model_nn represents the structure of the neural network.

For example: nn.Linear(1,2) means 1 input connected to 2 outputs.
The (x) input is a good example of this as it derives its value from
the (y) of the previous neuron and outputs to 2 activation function nodes.

Respectively, (2,2) is used for the hidden layer and (2,1) is used for
the final output (y) layer. 

Sequential() is simply a sequential container. Meaning that modules will
be added in the order they are passed.
"""
model_nn = nn.Sequential(
    nn.Linear(1,2),  # input layer (x)
    nn.ReLU(),       # activation function (in this case ReLU)
    nn.Linear(2,2),  # hidden layer (i.e. middle layers)
    nn.ReLU(),       # activation function (in this case ReLU)
    nn.Linear(2,1)   # output layer (y)
).to(device)

"""
torch.optim is a package implementing various optimization algorithms. To use
this method you have to construct an optimizer object (optL) that will hold
the current state and will update the parameters based on the computed gradients.

An EPOCH means tha you've trained the neural network exactly once with all of 
the data. 

A LEARNING RATE is a hyper-parameter that controls how quickly your network is
able to learn. Every time the network receives feedback from the supervisor it
learns what the correct answer should be. For reference on how to decide on this
value: https://towardsdatascience.com/how-to-decide-on-learning-rate-6b6996510c98 
"""
n_epochs = 2
learning_rate = 1e-2
optL = optim.SGD(model_nn.parameters(), lr=learning_rate)

"""
torch.nn.MSELoss() creates a criterion that measures the mean squared error 
between each element in the input (x) and the target (y).

size_average(bool) by default, the losses are averaged over each loss element
in the batch. If set to false, the losses are summed for each minibatch. 
Default=False. 

reduce(bool) by default, the losses are averaged or summed over observations
for each minibatch depending on size_average. If set to false, returns a loss
per batch element instead and ignores size_average.
Default=True

resuction(str) specifies the reduction to apply to the output:
    'none' means no reduction will be applied.
    'mean' means the sum of the output will be divided by the number of elements in the output.
    'sum' means the output will be summed.
Default='mean'
"""

loss_fn = torch.nn.MSELoss(size_average=False,reduce=False,reduction='sum')

# t_u is the input array
# numpy_to_variable() function converts it to gradient supported Tensor variable
t1_u = numpy_to_variable(t_u[:])

# Creates tensor t_ucol
t_ucol = torch.tensor(t1_u, device=device, requires_grad=True)

# Repeat for input t_c
t1_c = numpy_to_variable(t_c[:])
t_ccol = torch.tensor(t1_c, device=device, requires_grad=True)

"""
torch.cat() concatenates the given sequence of 'seq' tensors in the given dimension.

Think of this as a process that glues together N rubiks cubes along a specified color,
where color=dimension and the cube=tensor. 

torch.detach() returns a new tensor detached from the current graph. 
"""

for epochs in range(n_epochs):

    t_u1 = torch.cat([t_ucol.view((-1, 1))], dim=1)
    t_c1 = torch.cat([t_ccol.view((-1, 1))], dim=1)
   
    wt_L0 = model_nn[0].weight.detach().to('cpu').numpy()
    bias_L0 = model_nn[0].bias.detach().to('cpu').numpy()
    
    wt_L2 = model_nn[2].weight.detach().to('cpu').numpy()
    bias_L2 = model_nn[2].bias.detach().to('cpu').numpy()
    
    wt_L4 = model_nn[4].weight.detach().to('cpu').numpy()
    bias_L4 = model_nn[4].bias.detach().to('cpu').numpy()
    

    print(f"epoch:{epochs}, weight_input_layer: {wt_L0}")
    print(f"epoch:{epochs}, bias_input_layer: {bias_L0}")
    print(" ")
    
    print(f"epoch:{epochs}, weight_hidden_layer: {wt_L2}")
    print(f"epoch:{epochs}, bias_hidden_layer: {bias_L2}")
    print(" ")
    
    print(f"epoch:{epochs}, weight_output_layer: {wt_L4}")
    print(f"epoch:{epochs}, bias_output_layer: {bias_L4}")
    print(" ") 
    
    t_output = model_nn(t_u1)
    print("output:",t_output)
    
    loss_train = loss_fn(t_output,t_c1)
    print("loss:",loss_train)
    print(" ")
#
#  zero out gradients and compute gradients of loss with respect to
#  weights and biases.
#
    optL.zero_grad()
    loss_train.backward(retain_graph=True)

    gradw_L0 = model_nn[0].weight.grad.detach().to('cpu').numpy()
    gradb_L0 = model_nn[0].bias.grad.detach().to('cpu').numpy()

    gradw_L2 = model_nn[2].weight.grad.detach().to('cpu').numpy()
    gradb_L2 = model_nn[2].bias.grad.detach().to('cpu').numpy()

    gradw_L4 = model_nn[4].weight.grad.detach().to('cpu').numpy()
    gradb_L4 = model_nn[4].bias.grad.detach().to('cpu').numpy()

    print(f"epoch:{epochs}, grad_w_input_layer: {gradw_L0}")
    print(f"epoch:{epochs}, grad_b_input_layer: {gradb_L0}")
    print(" ")
    
    print(f"epoch:{epochs}, grad_w_hidden_layer: {gradw_L2}")
    print(f"epoch:{epochs}, grad_b_hidden_layer: {gradb_L2}")
    print(" ")

    print(f"epoch:{epochs}, gradw_output_layer: {gradw_L4}")
    print(f"epoch:{epochs}, gradb_output_layer: {gradb_L4}")
    print(" ") 

    curr_lr = optL.param_groups[0]["lr"]
    print("learning rate:",curr_lr)

    optL.step()
    
    print("###")