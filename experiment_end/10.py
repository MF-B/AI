import numpy as np
import torch
from torchvision import datasets
from torchvision import transforms
import matplotlib.pyplot as plt

train_dataset=datasets.MNIST(root='./data',train=True,transform=transforms.ToTensor(),download=True)
train_loader=torch.utils.data.DataLoader(train_dataset,batch_size=1,shuffle=False)
print('OK!',len(train_dataset),len(train_loader))
for step1,(x_train,y_train) in enumerate(train_loader):
    if step1 >= 3:
        break
    print(y_train)
    x_img=x_train.squeeze()
    plt.imshow(x_img.numpy(),cmap='gray')
    plt.show()

