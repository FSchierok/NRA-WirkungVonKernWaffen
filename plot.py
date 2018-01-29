import numpy as np
import matplotlib.pyplot as plt

rho_a = 1.147
rho_0 = 1.247


def overpres(r_sc):
    return (3.2 * 10**6 / r_sc**3 * np.sqrt(1 + (r_sc / 87)**2) * (1 + (r_sc / 800)))


def scaled_range(Y, r):
    return (rho_a / rho_0 / Y)**(1 / 3) * r


x = np.linspace(0.1, 5000, 1000)

plt.figure(1)
plt.plot(x, overpres(scaled_range(1000, x)))
plt.yscale("log")
plt.xlabel(r"$r\,/\, \mathrm{m} $")
plt.ylabel(r"$\Delta p \, /\,p_0$")
plt.axes([0.5, 0.5, 0.3, 0.3])
plt.plot(x, overpres(scaled_range(1000, x)))
plt.xlim(250, 750)
plt.ylim(10, 100)
plt.savefig("img/over.pdf")


def friedland(t, r, Y):
    return (P0 + overpres(scaled_range(Y, r)) * np.exp(-1 * t / t_0) * (1 - t / t_0))


P0 = 1
t_0 = 0.2
T = np.linspace(0, 1.5, 100)
plt.figure(2)
plt.plot(T, friedland(T, 300, 1000))
plt.xlabel(r"$t\,/\,\mathrm{s}$")
plt.ylabel(r"$P\,/\,Pa$")
plt.savefig("img/fried.pdf")
