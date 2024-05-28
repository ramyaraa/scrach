import matplotlib.pyplot as plt
import numpy as np

# Input Characteristics
V_BE = np.linspace(0.4, 0.8, 100)
I_B = [10**-15 * (np.exp(vbe / 0.025) - 1) for vbe in V_BE]

plt.figure(figsize=(10, 6))
plt.plot(V_BE, I_B, label='V_CE = 10V')
plt.xlabel('Base-Emitter Voltage (V_{BE}) [V]')
plt.ylabel('Base Current (I_B) [A]')
plt.title('Input Characteristics of CE Configuration')
plt.legend()
plt.grid(True)
plt.show()

# Output Characteristics
V_CE = np.linspace(0, 10, 100)
I_C = [0.02 * vce for vce in V_CE]

plt.figure(figsize=(10, 6))
for i in range(1, 5):
    plt.plot(V_CE, [i * 0.01 + 0.02 * vce for vce in V_CE], label=f'I_B = {i * 0.01}mA')
plt.xlabel('Collector-Emitter Voltage (V_{CE}) [V]')
plt.ylabel('Collector Current (I_C) [A]')
plt.title('Output Characteristics of CE Configuration')
plt.legend()
plt.grid(True)
plt.show()
