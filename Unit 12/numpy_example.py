# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Alex So
#               Garret Sumpter
#               Zane Aschenback
#               Clint Smith
# Section:      573
# Assignment:   Lab Topic 12 Team
# Date:         
#

# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

import numpy as np
import matplotlib as plt
from math import *
a = np.arange(12).reshape(3, 4)
b = np.arange(8).reshape(4, 2)
c = np.arange(6).reshape(2,3)
d = a @ b @ c
e = np.sqrt(d) / 2
print(f'A={a}\n')
print(f'B={b}\n')
print(f'C={c}\n')
print(f'D={d}\n')
print(f'E={e}')