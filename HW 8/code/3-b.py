#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created at Dec 17, 2016 13:06

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
from matplotlib.colors import LogNorm
import os

my_path = os.path.abspath(__file__ + "/../../")
plt.style.use("classic")

gamma_sigma = 1
gamma_pi = 1 / 3
gamma_d = 1 / 10
plot_points = 50
k = np.linspace(0, 1 / 2, num=plot_points, endpoint=True)


def dynamical_matix(kk1, kk2):
    d11 = 2 * gamma_sigma + 2 * gamma_pi + 4 * gamma_d - 2 * gamma_pi * np.cos(
        2 * np.pi * kk2) - 2 * gamma_sigma * np.cos(2 * np.pi * kk1) - 2 * gamma_d * (
        np.cos(2 * np.pi * (kk1 + kk2)) + np.cos(2 * np.pi * (kk1 - kk2)))
    d12 = -2 * gamma_d * (np.cos(2 * np.pi * (kk1 + kk2)) -
                          np.cos(2 * np.pi * (kk1 - kk2)))
    d21 = d12
    d22 = 2 * gamma_sigma + 2 * gamma_pi + 4 * gamma_d - 2 * gamma_sigma * np.cos(
        2 * np.pi * kk2) - 2 * gamma_pi * np.cos(2 * np.pi * kk1) - 2 * gamma_d * (
        np.cos(2 * np.pi * (kk1 + kk2)) + np.cos(2 * np.pi * (kk1 - kk2)))
    m = np.array([[d11, d12], [d21, d22]])
    return m


def eig_dynm_mat(kk1, kk2):
    eig_vals, eig_vecs = np.linalg.eig(dynamical_matix(kk1, kk2))
    return np.sort(eig_vals)


fig1 = plt.figure()
ax1 = plt.subplot(131)
plt.plot(k, [eig_dynm_mat(k1, 0) for k1 in k])  # (0,0)->(1/2,0)
plt.ylim((0, 6))
ax1.yaxis.tick_left()
ax1.set_yticks(range(1, 7))
xticks_pos_1 = [0, 1 / 2]
plt.xticks(xticks_pos_1, [r'$(0,0)$', r'$(0, \frac{1}{2})$'])
plt.ylabel(r'$\omega$', fontsize=14)


ax2 = plt.subplot(132)
plt.plot(k, [eig_dynm_mat(1 / 2, k2) for k2 in k])  # (1/2,0)->(1/2,1/2)
ax2.yaxis.set_ticklabels([])
plt.xticks([])
plt.ylim((0, 6))

ax3 = plt.subplot(133)
# (1/2,1/2)->(0,0), here the x-axis is inverted
plt.plot(k, [eig_dynm_mat(k1, k1) for k1 in np.flipud(k)])
# plt.yticks([])
plt.ylim((0, 6))
ax3.set_yticks(range(1, 7))
ax3.yaxis.tick_right()
xticks_pos_1 = [0, 1 / 2]
plt.xticks(xticks_pos_1, [r'$(\frac{1}{2}, \frac{1}{2})$', r'$(0, 0)$'])

plt.subplots_adjust(wspace=0, hspace=0)  # Remove spaces between subplots
plt.suptitle(r'Vibrational frequencies for the k-space path', fontsize=14)
# plt.show()
fig1.savefig(my_path + "/images/pro-3-b.pdf")

fig2 = plt.figure()
ax = fig2.add_subplot(111, projection='3d')
xv, yv = np.meshgrid(k, k)
ax.plot_surface(xv, yv, [[eig_dynm_mat(k1, k2)[0]
                          for k1 in k] for k2 in k])
fig2.savefig(my_path + "/images/pro-3-b-surface.pdf")
