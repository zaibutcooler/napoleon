import torch.nn as nn

class Agent(nn.Module):
    def __init__(self, ) -> None:
        super().__init__()
        self.model = nn.Sequential()

    def forward(self,x):
        result = self.model(x)
        return result