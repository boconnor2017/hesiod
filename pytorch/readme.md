# Terms and Definitions
| Term | Definition |
|------|------------|
| Vector | A term that refers to some quantities that cannot be expressed by a single number, or to elements of some vector spaces. |
| Vector Space | A set whose elements, often called vectors, may be added together and multiplied by numbers called scalars. Scalars are often real numbers, but can be complex numbers or generally an element of any field. The operations of vector addition and scalar multiplication must satisfy certain requirements called vector axioms. |
| Scalar | An element of a field which is used to define a vector space. In linear algebra, real numbers or general elements of a field are called scalars and relate to vectors in an associated vector space through the operation of scalar multiplication, in which a vector can be multiplied by a scalar in the defined way to produce another vector. |
| Tensor | An algebraic object that describes a multilinear relationship between sets of algebraic objects related to a vector space. Tensors may map between different objects such as vectors, scalars, and even other tensors. |
| Rise | How far a line goes UP. |
| Run | How far a line goes ALONG for a given distance. |
| Slope | Rise over Run |
| Derivative | A fundamental tool that quantifies the sensitivity of change of a function's output with respect to its input. The derivative of a function of a single variable at a chosen input value, when it exists, is the slope of the tangent line to the graph of the function at that point. |
| Partial Derivative | A derivative which holds some variables as constants. |
| Automatic Differentiation | A set of techniques to evaluate the partial derivative of a function specified by a computer program. |
| Polynomial | An expression involving addition, subtraction, multiplication, and positive-integer powers of variables. |
| Cubic Function | A function of the polynomial function of degree three. f(x) = ax^3 + bx^3 + cx + d |
| Forward Pass | The flow of information from the input to the output in a neural network. |
| Loss or Mean Squared Error | (L) is the square of the difference between the output value `y` and the known value `y`. MSE is a risk function, used to estimate an unobserved quantity. In machine learning MSE may refer to the average loss on an observed data set, which can be used to quantify the quality of an estimator. |

# Python Libraries
**Torch** (i.e. PyTorch) is a [library](https://pypi.org/project/torch/) that provides two main features:
1. An n-dimensional **Tensor**
2. Automatic differentiation for building and training neural networks

**NumPy** is a [library](https://numpy.org/) that provides an n-dimensional array object, and many functions for manipulating these arrays. Numpy is a generic framework for scientific computing. 

**Math** is a [library](https://docs.python.org/3/library/math.html) that provides access to the mathematical functions defined by C standard. 

**Random** is a [library](https://docs.python.org/3/library/random.html) that implements pseudo-random number generators for various distributions. Almost all modules from this library depend on the basic `random()` function which generates a random float uniformly in the half-open range `0.0 <= X < 1.0`.

# References
* [PyTorch Documentation](https://pytorch.org/)
* [Neural Networks, Forward Pass, and Backpropogation](https://towardsdatascience.com/neural-networks-forward-pass-and-backpropagation-be3b75a1cfcc)
