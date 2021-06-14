import numpy as np
data = np.genfromtxt('data/example_data.csv', delimiter=';',
                     names=True, dtype=None, encoding='UTF'
                     )
print(data)
