import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Grid setup (high resolution)
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)

# Dual voltage wells (one peak, one pit)
A1, sigma1, pos1 = 10, 1.0, (-3, -3)
A2, sigma2, pos2 = -6, 1.5, (4, 4)

V = (A1 * np.exp(-((X - pos1[0])**2 + (Y - pos1[1])**2) / (2 * sigma1**2)) +
     A2 * np.exp(-((X - pos2[0])**2 + (Y - pos2[1])**2) / (2 * sigma2**2)))

# Electric field = -grad(V)
Ey, Ex = np.gradient(-V)

# Plot voltage surface
fig = plt.figure(figsize=(14, 6))

ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.plot_surface(X, Y, V, cmap=cm.plasma)
ax1.set_title("SpacetimePotential: Dual Curvature (Einstein Test)")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("Voltage")

# Plot electric field vectors
ax2 = fig.add_subplot(1, 2, 2)
ax2.contourf(X, Y, V, levels=100, cmap=cm.plasma, alpha=0.7)
ax2.quiver(X[::10, ::10], Y[::10, ::10], Ex[::10, ::10], Ey[::10, ::10], color='black')
ax2.set_title("Electric Field (−∇V)")
ax2.set_xlabel("x")
ax2.set_ylabel("y")

plt.tight_layout()
plt.show()
