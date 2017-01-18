#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created at Dec 6, 2016 01:20

from __future__ import division
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

ep = 1 / 2
t = 1 / 4
a = 1
k_start = - 1 * np.pi / a  # Start point of wave vector
k_end = 1 * np.pi / a
k = np.linspace(k_start, k_end, num=500, endpoint=False)
e_1 = np.linspace(0.292893, 0.5, num=500, endpoint=False)
e_2 = np.linspace(1.5, 1.70711, num=500, endpoint=False)


def hamiltonian(kk):
    return np.array([[ep + 1, t * (1 + np.exp(-1j * kk * a))],
                     [t * (1 + np.exp(1j * kk * a)), ep]])


def eig_hamiltonian_upper_band(kk):
    eig_val, eig_vec = LA.eig(hamiltonian(kk))
    band_1 = [eig_val[0], eig_vec[0]]
    return band_1


def eig_hamiltonian_lower_band(kk):
    eig_val, eig_vec = LA.eig(hamiltonian(kk))
    band_2 = [eig_val[1], eig_vec[1]]
    return band_2


def density_of_states(ee):
    g = (32 * (ee - 1) / np.pi / np.sqrt(1 - (8 * (ee - 1) ** 2 - 3) ** 2))
    return np.abs(g)


# Energy range
band_1 = [eig_hamiltonian_lower_band(kk) for kk in k]
band_1_energy = [band_1[i][0] for i in range(len(band_1))]
band_2 = [eig_hamiltonian_upper_band(kk) for kk in k]
band_2_energy = [band_2[i][0] for i in range(len(band_2))]


def projected_density_of_states_1():
    g1 = np.array([density_of_states(ee) for ee in band_1_energy])
    c1_square = np.array([np.conj(band_1[i][1][0]) * band_1[i][1][0]
                          for i in range(len(band_1))])
    c2_square = np.array([np.conj(band_1[i][1][1]) * band_1[i][1][1]
                          for i in range(len(band_1))])
    g_d = g1 * c1_square
    g_p = g1 * c2_square
    return [g_d, g_p, g_d + g_p]


def projected_density_of_states_2():
    g2 = np.array([density_of_states(ee) for ee in band_2_energy])
    c1_square = np.array([np.conj(band_2[i][1][0]) * band_2[i][1][0]
                          for i in range(len(band_2))])
    c2_square = np.array([np.conj(band_2[i][1][1]) * band_2[i][1][1]
                          for i in range(len(band_2))])
    g_d = g2 * c1_square
    g_p = g2 * c2_square
    return [g_d, g_p, g_d + g_p]


plt.plot(e_1, [density_of_states(ee)+1 for ee in e_1], label="original lower band")
plt.plot(band_1_energy, projected_density_of_states_1()[0], label="lower band on d state")
plt.plot(band_1_energy, projected_density_of_states_1()[1], label="lower band on p state")
plt.plot(band_1_energy, projected_density_of_states_1()[2], label="lower p plus d state")
plt.plot(e_2, [density_of_states(ee)+1 for ee in e_2], label="original upper band")
plt.plot(band_2_energy, projected_density_of_states_2()[0], label="upper band on d state")
plt.plot(band_2_energy, projected_density_of_states_2()[1], label="upper band on p state")
plt.plot(band_2_energy, projected_density_of_states_2()[2], label="upper p plus d state")
plt.ylim((0, 60))
plt.xlabel(r'$\varepsilon$', fontsize=16)
plt.ylabel(r'$g(\varepsilon)$', fontsize=16)
plt.legend(loc="best")
# plt.show()
plt.savefig("/Users/Neo/Documents/APPH 6081/HW 7/images/pro_1_c.pdf")
