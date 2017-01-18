#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created at Dec 5, 2016 17:12

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

t = 0.25
ep = 0.5
a = 1
k = np.linspace(-np.pi / a, np.pi / a, num=500, endpoint=True)


def energy_approximation_1(kk):
    return 3 / 2 + t**2 * (2 * np.cos(kk * a) + 2)


def energy_approximation_2(kk):
    return 1 / 2 - t**2 * (2 * np.cos(kk * a) + 2)


def energy_1(kk):
    e = ep + 0.5 + 0.5 * np.sqrt((np.cos(kk * a / 2))**2 + 1)
    return e


def energy_2(kk):
    e = ep + 0.5 - 0.5 * np.sqrt((np.cos(kk * a / 2))**2 + 1)
    return e


# Exact values
plt.plot(k, [energy_1(kk) for kk in k], label="Upper analytical eigenvalue")
plt.plot(k, [energy_2(kk) for kk in k], label="Lower analytical eigenvalue")
# Approximation values
plt.plot(k, [energy_approximation_1(kk)
             for kk in k], label="Upper approximate eigenvalue")
plt.plot(k, [energy_approximation_2(kk)
             for kk in k], label="Lower approximate eigenvalue")
plt.xlim([-np.pi / a, np.pi / a])
plt.xlabel(r'$k$', fontsize=16)
plt.ylabel(r'$E$', fontsize=16)
k_locations = np.array(np.linspace(-np.pi / a, np.pi / a, 5))
plt.xticks(k_locations, [r'-$\frac{\pi}{a}$', r'$-\frac{\pi}{2a}$',
                         '$0$', r'$\frac{\pi}{2a}$', r'$\frac{\pi}{a}$'])
plt.legend(loc="best")
# plt.show()
plt.savefig("/Users/Neo/Documents/APPH 6081/HW 7/images/pro_1_d.pdf")
