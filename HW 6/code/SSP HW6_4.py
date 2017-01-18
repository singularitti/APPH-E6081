#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created at Nov 23, 2016 20:26

import numpy as np
import matplotlib.pyplot as plt
import functools

plot_points = 5000
x_00_05 = np.linspace(0, 0.5, plot_points)

v_00 = [0, 0]
v_10 = [1, 0]
v_b10 = [-1, 0]
v_01 = [0, 1]
v_0b1 = [0, -1]
v_11 = [1, 1]
v_b1b1 = [-1, -1]
v_1b1 = [1, -1]
v_b11 = [-1, 1]

prim_list = np.vstack((v_00, v_10, v_b10, v_01, v_0b1, v_11, v_b1b1, v_1b1, v_b11))
prim_matrix = np.array([(v_i - prim_list) for v_i in prim_list]).tolist()


def V_004():
    return -0.04


def V_002():
    return -0.02


def V_00():
    return 0


def V_others():
    return 0


def assign_matrix(x):
    if x == v_00:
        return V_00()
    elif x == v_10 or x == v_b10 or x == v_01 or x == v_0b1:
        return V_004()
    elif x == v_11 or x == v_b1b1 or x == v_1b1 or x == v_b11:
        return V_002()
    else:
        return V_others()


# 9x9 matrix for the potential
v = np.matrix([[assign_matrix(prim_matrix[i][j]) for j in range(0, 9)] for i in range(0, 9)])


# 9x9 matrix for the kinetic
def kinetic(x, y):
    return np.diag((x ** 2 + y ** 2, (x + 1) ** 2 + y ** 2, (x - 1) ** 2 + y ** 2, x ** 2 + (y + 1) ** 2,
                    x ** 2 + (y - 1) ** 2, (x + 1) ** 2 + (y + 1) ** 2,
                    (x - 1) ** 2 + (y - 1) ** 2, (x + 1) ** 2 + (y - 1) ** 2, (x - 1) ** 2 + (y + 1) ** 2))


# diagonalize hamil=h+v
def diagonalize_hamiltonian(x, y):
    eig_vals, eig_vecs = np.linalg.eig(kinetic(x, y) + v)
    return np.sort(eig_vals)  # The eigenvalues are not necessarily ordered, so need to be sorted.


# We need transpose because we need to connect eigenvalues in time period
hamil_00_05 = np.transpose(map(functools.partial(diagonalize_hamiltonian, y=0), x_00_05))

fig = plt.figure()
nine_by_nine = plt.plot(x_00_05, hamil_00_05[0], label="$9 \\times 9$ matrix branch")


# Free electron case
def free_diagonalize_hamiltonian(x, y):
    eig_vals, eig_vecs = np.linalg.eig(kinetic(x, y))
    return np.sort(eig_vals)  # The eigenvalues are not necessarily ordered, so need to be sorted.


free_hamil_00_05 = np.transpose(map(functools.partial(free_diagonalize_hamiltonian, y=0), x_00_05))

plt.plot(x_00_05, free_hamil_00_05[0], label="free electrons branch")


# Analytical eigenvalue of the lowest branch
def analytical_eig_val(kx, ky, order=0):
    mat = np.matrix([[kx ** 2 + ky ** 2, -0.04], [-0.04, (kx - 1) ** 2 + ky ** 2]])
    eig_vals, eig_vecs = np.linalg.eig(mat)
    return np.sort(eig_vals)[order]


ana_eig_val = [analytical_eig_val(xx, 0) for xx in x_00_05]
plt.plot(x_00_05, ana_eig_val, label="analytic eigenvalue for the lower branch")


# Second order correction
def analytical_eig_vecs(kx, ky):
    mat = np.matrix([[kx ** 2 + ky ** 2, -0.04], [-0.04, (kx - 1) ** 2 + ky ** 2]])
    eig_vals, eig_vecs = np.linalg.eig(mat)
    return np.abs(eig_vecs)[0]


def second_order_correction_of_energy(kx):
    val = analytical_eig_val(kx, 0)
    vecs = analytical_eig_vecs(kx, 0)
    h0 = kinetic(kx, 0)

    def step(j):
        return np.conj(vecs[0, 0] * v[j, 0] + vecs[0, 1] * v[j, 2]) * (vecs[0, 0] * v[j, 0] + vecs[0, 1] * v[j, 2]) / (
            val - h0[j, j])

    second_order_correction = [step(j) for j in range(3, 9)]
    return val + np.conj(vecs[0, 0] * v[1, 0] + vecs[0, 1] * v[1, 2]) * (
        vecs[0, 0] * v[1, 0] + vecs[0, 1] * v[1, 2]) / (val - h0[1, 1]) + np.sum(
        second_order_correction)


second = plt.plot(x_00_05, [second_order_correction_of_energy(xx) for xx in x_00_05], label="2nd order correction")
plt.xlabel("$k_x$", fontsize=16)
plt.ylabel("$E$", fontsize=16)
plt.ylim((-0.05, 0.28))
plt.legend(loc="best", fontsize=12)
plt.savefig("/Users/neo/Documents/APPH 6081/HW 6/images/pro_1_4.pdf")
