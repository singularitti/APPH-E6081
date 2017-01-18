#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created at Nov 25, 2016 11:36

import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

e0 = 0
t = 1
e = 0.05 * t
a = 1
h0 = np.array([[e0 + e, t], [t, e0 - e]])
h1 = np.array([[0, 0], [t, 0]])
hm1 = np.array([[0, t], [0, 0]])
kx = np.linspace(0, np.pi / a, 500)


def hamiltonian(k):
    return 0.5 * (h0 + np.exp(2.0j * k * a) * h1 + np.exp(-2.0j * k * a) * hm1)


def eig_val(k):
    eig_vals, eig_vecs = np.linalg.eig(hamiltonian(k))
    return np.real(np.sort(eig_vals))


plt.plot(kx, [eig_val(kk_xx) for kk_xx in kx])
plt.xlabel("$k$", fontsize=16)
plt.ylabel("$E$", fontsize=16)
plt.xlim((0, np.pi / a))
plt.ylim((-1.05, 1.05))
k_locations = np.array(np.linspace(0, np.pi / a, 3))
plt.xticks(k_locations, ['$0$', r'$\frac{\pi}{2a}$', r'$\frac{\pi}{a}$'])
plt.savefig("/Users/neo/Documents/APPH 6081/HW 6/images/pro_2.pdf")
