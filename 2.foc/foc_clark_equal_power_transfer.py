import numpy as np
import matplotlib.pyplot as plt

alphad = np.arange(0, 360, 1)
alpha = np.deg2rad(alphad)

va = np.cos(alpha)
vb = np.sin(alpha)

# inv clark
a = va
b = vb * 0.8660254039 - 0.5 * va
c = -(a + b)

k = 2 / np.sqrt(3)

ta = k * a
tb = k * b
tc = -(ta + tb)

ra = va - (1 / np.sqrt(3)) * vb
rb = (2 / np.sqrt(3)) * vb
rc = -(ra + rb)

plt.figure(1)
plt.subplot(221)
plt.plot(alphad, a, color="r", label="a")
plt.plot(alphad, b, color="g", label="b")
plt.plot(alphad, c, color="b", label="c")

plt.subplot(222)
plt.plot(alphad, ta, color="r", label="a")
plt.plot(alphad, tb, color="g", label="b")
plt.plot(alphad, tc, color="b", label="c")

plt.subplot(223)
plt.plot(alphad, ra, color="r", label="a")
plt.plot(alphad, rb, color="g", label="b")
plt.plot(alphad, rc, color="b", label="c")

print()

plt.show()
