import torch 
import numpy as np 

data = [[1, 2],[3, 4]]
x_data = torch.tensor(data)

print(x_data)
print("")

tensor = torch.rand(3,4)

print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")
print("")

t1 = torch.cat([tensor, tensor, tensor], dim=1)
print(t1)