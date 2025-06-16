import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Wave Energy", page_icon="⚡")

st.title("⚡ Wave Energy Analysis")
st.markdown("Visualize **Kinetic** and **Potential** energy of a wave on a string over space and time.")

# Parameters
x = np.linspace(0, 1, 100)
t = st.slider("Time (t)", 0.0, 10.0, 1.0, step=0.1)
wave_amplitude = st.slider("Wave Amplitude", 0.1, 2.0, 1.0)
wave_speed = st.slider("Wave Speed", 0.5, 5.0, 1.0)

# Wave function
u = wave_amplitude * np.sin(2 * np.pi * (x - wave_speed * t))

# Energy calculations
velocity = -2 * np.pi * wave_speed * wave_amplitude * np.cos(2 * np.pi * (x - wave_speed * t))
kinetic_energy = 0.5 * velocity**2
potential_energy = 0.5 * (np.gradient(u, x))**2
total_energy = kinetic_energy + potential_energy

# Plotting
fig, ax = plt.subplots()
ax.plot(x, kinetic_energy, label="Kinetic Energy", color='orange')
ax.plot(x, potential_energy, label="Potential Energy", color='blue')
ax.plot(x, total_energy, label="Total Energy", color='green')
ax.set_xlabel("x")
ax.set_ylabel("Energy")
ax.set_title("Energy Distribution at t = {:.1f}".format(t))
ax.legend()
ax.grid(True)

st.pyplot(fig)

st.markdown("---")
st.success("Energy is conserved across the wave — observe how kinetic and potential energies evolve!")