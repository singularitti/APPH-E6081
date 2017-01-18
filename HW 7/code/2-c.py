#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created at Dec 4, 2016 18:56

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


t = 2.5
a = 1


def eigenvalue(k1, k2):
    # h12 = t * (np.exp(2j * np.pi * (-1 / 3 * k1 - 1 / 3 * k2)) +
    #            np.exp(2j * np.pi * (2 / 3 * k1 - 1 / 3 * k2)) +
    #            np.exp(2j * np.pi * (-1 / 3 * k1 + 2 / 3 * k2)))
    # h21 = np.conj(h12)
    # return np.sqrt(h12 * h21)
    return t * np.sqrt(3 + 4 * np.cos(3 * k1 / 2 * a) *
                       np.cos(np.sqrt(3) * k2 / 2 * a)
                       + 2 * np.cos(np.sqrt(3) * k2 * a))


Fermi_energy = eigenvalue(2 * np.pi / 3 / a, 2 * np.pi / 3 / np.sqrt(3) / a)
