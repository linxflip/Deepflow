import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim as SGD

def main():
    # input
    # creates a tensor - data in a range
    input_doses = torch.linspace(start=0, end=1, steps=10)

    model = indexNN()
    output_values

class indexNN(nn.module):
    def __init__(self):
        super().__init__()
        # initialize thr weights and biases
        # layer 0
        self.w00 = nn.Parameter(torch.tensor(1.7), requires_grad=False)
        self.b00 = nn.Parameter(torch.tensor(1.7), requires_grad=False)
        self.w01 = nn.Parameter(torch.tensor(1.7), requires_grad=False)

        # layer 1
        self.w10 = nn.Parameter(torch.tensor(1.7), requires_grad=False)
        self.b10 = nn.Parameter(torch.tensor(1.7), requires_grad=False)
        self.w11 = nn.Parameter(torch.tensor(1.7), requires_grad=False)

        self.final_bias = nn.Parameter(torch.tensor(-16), requires_grad=False)
    # connects the nodes to activation functions to more nodes
    def forward(self, input):
        input_to_relu_01 = input * self.w00 + self.b00
        relu_01_output = F.relu(input_to relu_01)
        scaled_relu_01 = relu_01_output * self w01

        input_to_relu_02 = input * self.w10 + self.b01
        relu_02_output = F.relu(input_to relu_02)
        scaled_relu_02 = relu_02_output * self w11

        input_to_final_relu = scaled_relu_01 + scaled_relu_02 + self.final_bias

        output = F.relu(input_to_final_relu)
        return output

main()