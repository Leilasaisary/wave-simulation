import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Wave Packet", layout="wide")

# Title
st.title("💊 Wave Packet Simulation")
st.markdown("""
A **wave packet** is a short *'burst'* or *'envelope'* of localized wave action that travels as a unit.
This simulation shows the **superposition of sine waves** to form a wave packet.
""")

# Parameters
col1, col2 = st.columns(2)

with col1:
    A = st.slider("Amplitude", 0.5, 5.0, 1.0)
    k0 = st.slider("Central Wavenumber k₀", 1.0, 20.0, 5.0)
    sigma_k = st.slider("Wavenumber Width σₖ", 0.1, 5.0, 1.0)

with col2:
    omega0 = st.slider("Central Frequency ω₀", 1.0, 20.0, 10.0)
    sigma_omega = st.slider("Frequency Spread σ_ω", 0.1, 5.0, 1.0)
    T = st.slider("Simulation Duration", 1.0, 10.0, 5.0)

# Coordinates
x = np.linspace(-20, 20, 500)
t = np.linspace(0, T, 200)
X, T_grid = np.meshgrid(x, t)

# Wave Packet Calculation
envelope = A * np.exp(-((X - 2 * T_grid)**2) / (2 * sigma_k**2))
carrier = np.cos(k0 * X - omega0 * T_grid)
wave = envelope * carrier

# Plot
fig, ax = plt.subplots(figsize=(10, 5))
c = ax.pcolormesh(X, T_grid, wave, shading='auto', cmap='plasma')
fig.colorbar(c, ax=ax, label='Amplitude')
ax.set_title("Wave Packet Evolution Over Time")
ax.set_xlabel("Position (x)")
ax.set_ylabel("Time (t)")

st.pyplot(fig)

# Explanation
st.markdown("""
---  
ℹ️ A wave packet combines multiple frequency components to produce a localized pulse.  
The packet travels and spreads over time, depending on the width of the frequency spectrum.

- **Envelope**: Defines localization.
- **Carrier wave**: Defines oscillations.
""")
