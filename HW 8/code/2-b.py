#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created at Dec 18, 2016 16:58


from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import os

my_path = os.path.abspath(__file__ + "/../../")
plt.style.use("classic")

a = 1
gamma = 200
d = np.linspace(-0.5, 0.5, 500, endpoint=True)


def e_electron(delta):
    return - 16 * a * delta / np.pi


def e_phonon(delta):
    return 2 * gamma * delta ** 2


plt.plot(d, [e_electron(dd) + e_phonon(dd) for dd in d])
plt.xlabel(r'$\delta$', fontsize=14)
plt.ylabel(r'$E_{\mathrm{total}}$')
plt.xlim((-0.5, 0.5))
plt.ylim((0, 100))
# plt.show()
plt.savefig(my_path + "/images/pro-2.pdf")
