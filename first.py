import numpy as np

import torch

import time

start = time.time()

print(np.random.randn(3,2) * np.random.rand(3,2))

end = time.time()

print(end-start)
