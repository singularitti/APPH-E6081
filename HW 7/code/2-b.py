#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created at Dec 4, 2016 11:02

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
from matplotlib.colors import LogNorm

plt.style.use("classic")

t = 2.5
a = 1
# Gamma point to M point
k_GM = np.linspace(0, 2 * np.pi / 3 / a, 500, endpoint=True)
# M point to K point
k_MK = np.linspace(0, 2 * np.pi / 3 / np.sqrt(3) / a, 500, endpoint=True)
# K point back to Gamma point
k_KG = np.linspace(2 * np.pi / 3 / a, 0, 500, endpoint=True)
k = np.linspace(-3 * np.sqrt(3), 3 * np.sqrt(3), 500, endpoint=True)


def eigenvalue(k1, k2):
    # h12 = t * (np.exp(2j * np.pi * (- k1 * a)) +
    #            np.exp(2j * np.pi * (k1 * a / 2 - np.sqrt(3) / 2 * k2)) +
    #            np.exp(2j * np.pi * (k1 * a / 2 + np.sqrt(3) / 2 * k2)))
    # h21 = np.conj(h12)  # Complex conjugte
    # return np.sqrt(h12 * h21)
    return t * np.sqrt(3 + 4 * np.cos(3 * k1 / 2 * a) *
                       np.cos(np.sqrt(3) * k2 / 2 * a)
                       + 2 * np.cos(np.sqrt(3) * k2 * a))


# Contour plot of band structure
# fig1 = plt.figure()
# xv, yv = np.meshgrid(k, k)
# plt.contour(xv, yv, [[eigenvalue(k1, k2)
#                       for k1 in k] for k2 in k], 20)
# Density plot of band structure
fig1 = plt.figure()
xv, yv = np.meshgrid(k, k)
plt.pcolormesh(xv, yv, [[eigenvalue(k1, k2)
                         for k1 in k] for k2 in k])
plt.xlim((-5, 5))
plt.ylim((-5, 5))

# Plot along the k-path
fig2 = plt.figure()
# Gamma to M path
ax1 = plt.subplot(131)
plt.plot(k_GM, [(eigenvalue(kx, 0), - eigenvalue(kx, 0)) for kx in k_GM])
plt.xlim((0, 2 * np.pi / 3 / a))
xticks_pos_1 = [0, 2 * np.pi / 3 / a]
plt.xticks(xticks_pos_1, [r'$\Gamma$', r'$\mathrm{M}$'])
ax1.yaxis.tick_left()
# M to K path
ax2 = plt.subplot(132)
plt.plot(k_MK, [(eigenvalue(2 * np.pi / 3 / a, ky),
                 - eigenvalue(2 * np.pi / 3 / a, ky)) for ky in k_MK])
plt.xlim((0, 2 * np.pi / 3 / np.sqrt(3) / a))
plt.ylim((-8, 8))
plt.yticks([])
xticks_pos_2 = [2 * np.pi / 3 / np.sqrt(3) / a]
plt.xticks(xticks_pos_2, [r'$\mathrm{K}$'])
# K back to Gamma path
ax3 = plt.subplot(133)
plt.plot(k_KG, [(eigenvalue(kx, kx / np.sqrt(3)),
                 - eigenvalue(kx, kx / np.sqrt(3))) for kx in k_KG])
plt.xlim((2 * np.pi / 3 / a, 0))
xticks_pos_3 = [0]
plt.xticks(xticks_pos_3, [r'$\Gamma$'])
ax3.yaxis.tick_right()
plt.subplots_adjust(wspace=0, hspace=0)  # Remove spaces between subplots
# print eigenvalue(0, 0)  # G point
# print eigenvalue(2 * np.pi / 3 / a, 0)  # M point
# print eigenvalue(2 * np.pi / 3 / a, 2 * np.pi / 3 / np.sqrt(3) / a)  # K
# point
# plt.show()
fig1.savefig("../images/pro-2-b-1.pdf")
fig2.savefig("../images/pro-2-b-2.pdf")
