import numpy as np
import torch

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
my_tensor = torch.from_numpy(data)
my_array = my_tensor.numpy()
my_list = my_tensor.tolist()
print(my_tensor)
print(my_array)
print(my_list)