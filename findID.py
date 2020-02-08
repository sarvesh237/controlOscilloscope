import visa
import numpy as np
import time
import matplotlib.pyplot as plt
rm = visa.ResourceManager('@py')
print(rm.list_resources())
