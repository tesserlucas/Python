import numpy as np
import matplotlib.pyplot as plt

# Define the time interval from 0 to 20 seconds
t = np.linspace(0, 20, 400)

# Define the functions
x1 = 20 * np.cos(0.2 * np.pi * t)
x2 = 10 * np.cos(0.2 * np.pi * t)
x3 = 10 * np.cos(0.4 * np.pi * t)
x4 = 10 * np.cos(0.2 * np.pi * t + np.pi / 2)
x5 = 10 * np.cos(0.2 * np.pi * t + np.pi / 4)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, x1, label='x = 20cos(0.2πt)')
plt.plot(t, x2, label='x = 10cos(0.2πt)')
plt.plot(t, x3, label='x = 10cos(0.4πt)')
plt.plot(t, x4, label='x = 10cos(0.2πt + π/2)')
plt.plot(t, x5, label='x = 10cos(0.2πt + π/4)')

plt.title('Position (cm) vs Time (s)')
plt.xlabel('Time (s)')
plt.ylabel('Position (cm)')
plt.legend()
plt.grid(True)
plt.show()
