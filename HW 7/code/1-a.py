#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created at Dec 2, 2016 16:30

import numpy as np
import matplotlib.pyplot as plt

ep = 0.5
t = 0.25
a = 1  # FBZ location
k = np.linspace(-np.pi / a, np.pi / a, num=500, endpoint=True)


def energy_1(kk):
    e = ep + 0.5 + 0.5 * np.sqrt((np.cos(kk * a / 2))**2 + 1)
    return e


def energy_2(kk):
    e = ep + 0.5 - 0.5 * np.sqrt((np.cos(kk * a / 2))**2 + 1)
    return e


plt.plot(k, [energy_1(kk) for kk in k])
plt.plot(k, [energy_2(kk) for kk in k])
plt.xlim([-np.pi / a, np.pi / a])
plt.xlabel(r'$k$', fontsize=16)
plt.ylabel(r'$\varepsilon$', fontsize=16)
k_locations = np.array(np.linspace(-np.pi / a, np.pi / a, 5))
plt.xticks(k_locations, [r'-$\frac{\pi}{a}$', r'$-\frac{\pi}{2a}$',
                         '$0$', r'$\frac{\pi}{2a}$', r'$\frac{\pi}{a}$'])
plt.show()
# plt.savefig("/Users/Neo/Documents/APPH 6081/HW 7/images/pro_1_a.pdf")
