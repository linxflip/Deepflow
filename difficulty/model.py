import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim as SGD

# parameters

# convolution layer 
class indexNN(nn.module):
    def __init__(self):
        super().__init__()
        # initialize thr weights and biases
        self.w00 = nn.Parameter(torch.tensor(1.7), requires_grad=False)
        self.b00 = nn.Parameter(torch.tensor(1.7), requires_grad=False)

# fully connected layer

# output
