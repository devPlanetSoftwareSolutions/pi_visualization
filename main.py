import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

theta_max = 1000
step = 0.01

theta = np.arange(0, theta_max, step)
z = np.exp(1j * theta) + np.exp(1j * theta * np.pi)
x = np.real(z)
y = np.imag(z)

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('#00001a')
fig.patch.set_facecolor('#00001a')

ax.set_xlim([-2.5, 2.5])
ax.set_ylim([-2.5, 2.5])

ax.set_title(r"Visualization of $z(\theta) = e^{i\theta} + e^{i\theta\pi}$", color='white', fontsize=16)
ax.set_xlabel("Re(z)", color='white', fontsize=14)
ax.set_ylabel("Im(z)", color='white', fontsize=14)

ax.grid(True, color='lightblue', linestyle='--', linewidth=0.5)

ax.set_aspect('equal')

ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

line, = ax.plot([], [], color='white', linewidth=0.5)

point, = ax.plot([], [], 'ro', markersize=5)

credits_text = ax.text(0.5, -0.1, "devPlanet Software Solutions", color='white', fontsize=8, ha='center', va='center', transform=ax.transAxes)

def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

def animate(i):
    line.set_data(x[:i], y[:i])
    point.set_data([x[i]], [y[i]])
    return line, point

ani = FuncAnimation(
    fig, animate, frames=len(theta), init_func=init, blit=True, interval=10, repeat=False
)

output_file = "pi_visualization.mp4"
writer = "ffmpeg"
fps = 60
ani.save(output_file, writer=writer, fps=fps)

print(f"Animation saved as {output_file}")
