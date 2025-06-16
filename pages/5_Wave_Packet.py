import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Wave Packet", page_icon="🎁")

st.title("🎁 Wave Packet Simulation")
st.markdown("This simulation shows how a wave packet is formed by the superposition of multiple sine waves.")

# Parameters
x = np.linspace(-20, 20, 1000)
k0 = st.slider("Central Wavenumber (k₀)", min_value=1.0, max_value=10.0, value=5.0)
dk = st.slider("Spread of Wavenumber (Δk)", min_value=0.1, max_value=5.0, value=1.0)
t = st.slider("Time (t)", min_value=0.0, max_value=10.0, value=0.0)

# Create wave packet
packet = np.exp(-(x**2) * dk**2) * np.cos(k0 * x - t)

# Plotting
fig, ax = plt.subplots()
ax.plot(x, packet, color='purple')
ax.set_title("Wave Packet at t = {:.2f}".format(t))
ax.set_xlabel("x")
ax.set_ylabel("Amplitude")
ax.grid(True)

st.pyplot(fig)

st.markdown("---")
st.info("Wave packets represent particles in quantum mechanics and are crucial for group velocity analysis.")