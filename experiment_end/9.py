import torch
tc = torch.arange(12)
print(tc)
t322 = tc.reshape(3, 2, 2)
print(t322)
t43 = tc.reshape(4, 3)
print(t43)
t234 = torch.arange(24).reshape(2, -1,4)
print(t234)
t1 = t322.reshape(-1)
print(t1)

t = torch.arange(24).reshape(2, 1, 3, 1, 4)
ts = t.squeeze()
print(ts.size)

t = torch.arange(24).reshape(2, 3, 4)
tus = t.unsqueeze(dim=2)
print(tus.size())