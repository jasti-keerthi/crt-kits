#shape/reshape
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print("reshape:",a.reshape(5,1))
print("shape:",a.shape)
print("type:",a.dtype)
print("astype:",a.astype(float))