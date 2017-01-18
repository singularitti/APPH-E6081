#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created at Dec 5, 2016 23:20

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

ep = 0.5
e_1 = np.linspace(0.292893, 0.5, num=500, endpoint=False)
e_2 = np.linspace(1.5, 1.70711, num=500, endpoint=False)


def density_of_states_1(e):
    g = - 32 * (e - 1) / np.pi / np.sqrt(1 - (8 * (e - 1)**2 - 3)**2)
    return g


def density_of_states_2(e):
    return 32 * (e - 1) / np.pi / np.sqrt(1 - (8 * (e - 1)**2 - 3)**2)


plt.plot(e_1, [density_of_states_1(ee) for ee in e_1])
plt.plot(e_2, [density_of_states_2(ee) for ee in e_2])
plt.xlabel(r'$\varepsilon$', fontsize=16)
plt.ylabel(r'$g(\varepsilon)$', fontsize=16)
plt.ylim((0, 60))
plt.show()
# plt.savefig("/Users/Neo/Documents/APPH 6081/HW 7/images/pro_1_b.pdf")
