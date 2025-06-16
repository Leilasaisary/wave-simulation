import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

st.set_page_config(page_title="1D Wave Simulation", layout="wide")

st.title("🌊 1D Wave Simulation")
st.markdown("Configure the wave parameters and observe a beautiful animation and energy plots.")

# --- Sidebar Parameters ---
st.sidebar.header("⚙️ Wave Settings")
wave_type = st.sidebar.selectbox("Wave Type", ["Standing Wave", "Traveling Wave"])
amplitude = st.sidebar.slider("Amplitude (A)", 0.1, 5.0, 1.0)
wavelength = st.sidebar.slider("Wavelength (λ)", 0.5, 5.0, 2.0)
speed = st.sidebar.slider("Wave Speed (v)", 0.5, 5.0, 1.0)
duration = st.sidebar.slider("Animation Duration (s)", 2, 10, 5)

st.sidebar.markdown("Created with ❤️ as part of the global **WaveLab Project**")

# --- Space and Time ---
x = np.linspace(0, 10, 200)
t_values = np.linspace(0, duration, 100)
X, T = np.meshgrid(x, t_values)

# --- Wave Calculation ---
if wave_type == "Standing Wave":
    Y = amplitude * np.sin(2 * np.pi * x / wavelength) * np.cos(2 * np.pi * speed * T / wavelength)
else:  # Traveling Wave
    Y = amplitude * np.sin(2 * np.pi * (X - speed * T) / wavelength)

# --- Energy Computation ---
kinetic_energy = 0.5 * (2 * np.pi * amplitude / wavelength) ** 2 * np.cos(2 * np.pi * speed * T / wavelength) ** 2
potential_energy = 0.5 * (2 * np.pi * amplitude / wavelength) ** 2 * np.sin(2 * np.pi * X / wavelength) ** 2

# --- 3D Wave Surface Plot ---
st.subheader("🎥 Wave Over Time (3D Plot)")

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')
surface = ax.plot_surface(X, T, Y, cmap=cm.viridis)
ax.set_xlabel("Position (x)")
ax.set_ylabel("Time (t)")
ax.set_zlabel("Amplitude")
st.pyplot(fig)

# --- Energy Plot ---
st.subheader("⚡ Wave Energy Over Time")

fig2, ax2 = plt.subplots(figsize=(8, 3))
ax2.plot(t_values, kinetic_energy.mean(axis=1), label="Kinetic Energy", color='blue')
ax2.plot(t_values, potential_energy.mean(axis=1), label="Potential Energy", color='red')
ax2.set_xlabel("Time (t)")
ax2.set_ylabel("Energy")
ax2.legend()
ax2.grid(True)
st.pyplot(fig2)
