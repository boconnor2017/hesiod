import torch 
import numpy as np 

"""
A tensor (in plain english) is a list of lists. a.k.a. a multi-dimensional array.

If you were to draw a tensor on a whiteboard it might look something like this:

    tensor a = [1, 2, 3...] # 1-dimensional array a.k.a your standard list
    tensor b = [[1, 2, 3...], [1, 2, 3...], [1, 2, 3...]] # 2-dimensional array a.k.a. your standard matrix
    tensor c = [[[1, 2, 3...], [1, 2, 3...], [1, 2, 3...]], [[1, 2, 3...], [1, 2, 3...], [1, 2, 3...]]]
    tensor d = [[[[1, 2, 3...], [1, 2, 3...], [1, 2, 3...]], [[1, 2, 3...], [1, 2, 3...], [1, 2, 3...]]], [[[1, 2, 3...], [1, 2, 3...], [1, 2, 3...]], [[1, 2, 3...], [1, 2, 3...], [1, 2, 3...]]], [[[1, 2, 3...], [1, 2, 3...], [1, 2, 3...]], [[1, 2, 3...], [1, 2, 3...], [1, 2, 3...]]]]
    ...

A tensor can have N dimensions. 
Tensors with the same "shape" (i.e. dimensions) can be used as variables in a algebraic formula.

Don't confuse tensors (physics) with tensors (computer science). Altough the math may be similar
the applications and the language are very different. If you lookup information about tensors
just make sure you know the context of the definition. 

torch.rand(size): Returns a tensor filled with random numbers from a uniform distribution. 
    Parameters:
        size(integer) is a sequence of integers defining the shape of the output tensor.
            Can be a variable number of arguments or a collection (i.e. a list or another tensor).

torch.cat(tensors, dim=0, *, out=None): Concatenates the given sequence of tensors in the 
    given dimension. All tensors must either have the same shape or be a 1-D empty tensor 
    with size (0,)
    Parameters:
        tensors(sequence of tensors) are any pothon sequence of tensors of the same shape.
        dim(int, optional) the dimension over which the sensors are concatenated.
        out(int, optional) the output tensor.
    
"""
print("Tensor A:")
tensor_a = torch.rand(0, )

print(f"Shape of tensor: {tensor_a.shape}")
print(f"Datatype of tensor: {tensor_a.dtype}")
print(f"Device tensor is stored on: {tensor_a.device}")
print("Hesiod's notes: its an empty tensor.")
print("")

ta = torch.cat([tensor_a, tensor_a, tensor_a])
print(ta)
print("")
print("")
print("")

print("Tensor B:")
tensor_b = torch.rand(1)

print(f"Shape of tensor: {tensor_b.shape}")
print(f"Datatype of tensor: {tensor_b.dtype}")
print(f"Device tensor is stored on: {tensor_b.device}")
print("Hesiod's notes: all numbers are the same because there is no range.")
print("")

tb = torch.cat([tensor_b, tensor_b, tensor_b])
print(tb)
print("")
print("")
print("")

print("Tensor C:")
tensor_c = torch.rand(1, 2)

print(f"Shape of tensor: {tensor_c.shape}")
print(f"Datatype of tensor: {tensor_c.dtype}")
print(f"Device tensor is stored on: {tensor_c.device}")
print("Hesiod's notes: now there is a range (notice how the number of brackets has changed), but the numbers aren't unique...")
print("")

tc = torch.cat([tensor_c, tensor_c, tensor_c])
print(tc)
print("")
print("")
print("")

print("Tensor D:")
tensor_d = torch.rand(1, 2)

print(f"Shape of tensor: {tensor_d.shape}")
print(f"Datatype of tensor: {tensor_d.dtype}")
print(f"Device tensor is stored on: {tensor_d.device}")
print("Hesiod's notes: ...so we set dim=1 (if you set it to 2, you will get an error!)... but the numbers are still pretty repetitive...")
print("")

td = torch.cat([tensor_d, tensor_d, tensor_d], 1)
print(td)
print("")
print("")
print("")

print("Tensor E:")
tensor_e = torch.rand(2, 900)

print(f"Shape of tensor: {tensor_e.shape}")
print(f"Datatype of tensor: {tensor_e.dtype}")
print(f"Device tensor is stored on: {tensor_e.device}")
print("Hesiod's notes: ...so we use bigger numbers in the range. This changes both the uniqueness of the numbers and the size of the list.")
print("")

te = torch.cat([tensor_e, tensor_e, tensor_e], 1)
print(te)
print("")
print("")
print("")

print("Tensor F:")
tensor_f = torch.rand(1, 2, 3)

print(f"Shape of tensor: {tensor_f.shape}")
print(f"Datatype of tensor: {tensor_f.dtype}")
print(f"Device tensor is stored on: {tensor_f.device}")
print("Hesiod's notes: more numbers in the size means we can set dim=2 without errors. Notice the number of brackets has changed.")
print("")

tf = torch.cat([tensor_f, tensor_f, tensor_f], 2)
print(tf)
print("")
print("")
print("")

print("Tensor G:")
tensor_g = torch.rand(18, 19, 20)

print(f"Shape of tensor: {tensor_g.shape}")
print(f"Datatype of tensor: {tensor_g.dtype}")
print(f"Device tensor is stored on: {tensor_g.device}")
print("Hesiod's notes: Big size, no dim.")
print("")

tg = torch.cat([tensor_g, tensor_g, tensor_g])
print(tg)
print("")
print("")
print("")

print("Tensor H:")
tensor_g = torch.rand(18, 19, 20)

print(f"Shape of tensor: {tensor_g.shape}")
print(f"Datatype of tensor: {tensor_g.dtype}")
print(f"Device tensor is stored on: {tensor_g.device}")
print("Hesiod's notes: same tensor, dim=1.")
print("")

th = torch.cat([tensor_g, tensor_g, tensor_g], 1)
print(th)
print("")
print("")
print("")

