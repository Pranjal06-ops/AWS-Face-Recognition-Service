import torch
class DummyCNN:
    def eval(self):
        pass
    def __call__(self, x):
        return torch.tensor([[0,1]])  # always predicts class 1