import os
import torch
import random

from collections import deque
from torch.utils.data import Dataset


class WaveNetDataset(Dataset):
    
    def __init__(self):
        self.data = []
        self.files = []
        self.visited = []
        self.frontier = deque([])
    
    def load_data(self, dst='data', wave_ext='wav'):
        for root, dirs, files in os.walk(dst):
            for f in files:
                if f.split('.')[-1] == wave_ext:
                    self.files.append(os.path.join(root, f))

    def extract_waves(self):
        raise NotImplementedError
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __len__(self):
        return len(self.data)



if __name__ == '__main__':
    ds = WaveNetDataset()
    ds.load_data()

    for i in ds.files:
        print(i)

