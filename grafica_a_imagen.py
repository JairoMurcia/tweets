# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:44:26 2019

@author: Estudiantes
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

plt.plot([1,2,3], [1,2,3], 'go-', label='line 1', linewidth=2)

plt.savefig("ejemplo.jpg")