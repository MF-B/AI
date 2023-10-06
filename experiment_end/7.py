import torch

t2 = torch.tensor([[0, 1, 2], [3, 4, 5]])
print(t2)
print(t2+1)
print(t2.size())
print(t2.dim())
print(t2.numel())
print(t2.dtype)

t_int8=torch.tensor([1.8,2],dtype=torch.int8)
print(t_int8)
t_float16=torch.tensor([1.8,2],dtype=torch.float16)
print(t_float16)


t3 = torch.empty(2)
print(t3)
t3 = torch.zeros(2,4)
print(t3)
t3 = torch.ones(2,3,4)
print(t3)
t3 = torch.full((2,4),3)
print(t3)