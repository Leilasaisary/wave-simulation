import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Wave Energy", layout="wide")

st.title("⚡ Energy of the Wave Over Time")

st.markdown("""
This module calculates and visualizes the **total mechanical energy** of a vibrating string over time.

The total energy includes:
- **Kinetic energy**: due to movement
- **Potential energy**: due to string deformation

We assume the wave is modeled by:
$$ u(x,t) = A \\cdot \\sin(\\pi x) \\cdot \\cos(\\omega t) $$
""")

# Parameters
L = st.slider("String length (L)", 0.5, 5.0, 1.0)
A = st.slider("Amplitude (A)", 0.1, 1.0, 0.5)
omega = st.slider("Frequency (ω)", 1.0, 10.0, 5.0)
rho = 1.0  # mass density
T = 1.0    # tension

# Time simulation
t = np.linspace(0, 5, 200)
x = np.linspace(0, L, 200)

# Energy computation
U = A * np.sin(np.pi * x[:, None] / L) * np.cos(omega * t)
velocity = -A * omega * np.sin(np.pi * x[:, None] / L) * np.sin(omega * t)
KE = 0.5 * rho * velocity**2
PE = 0.5 * T * (np.gradient(U, axis=0))**2

total_energy = KE.sum(axis=0) + PE.sum(axis=0)

# Plot
fig, ax = plt.subplots()
ax.plot(t, total_energy, color='orange')
ax.set_xlabel("Time (s)")
ax.set_ylabel("Total Energy")
ax.set_title("🔋 Energy of the Wave Over Time")

st.pyplot(fig)