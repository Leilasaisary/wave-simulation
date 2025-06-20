import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Page configuration
st.set_page_config(page_title="🌊 Wave: 1D Simulation", layout="wide")

# Title
st.title("🌈 1D Wave Simulation — Explore Vibrations on a String")
st.markdown("""
Visualize how waves evolve over space and time using colorful 3D plots and energy analysis.

Dive into the fascinating physics of wave motion with mathematical explanations and real-life analogies.

---
""")

# --- Theory Section ---
with st.expander("📘 Theory & Real-Life Applications", expanded=True):
    st.markdown(r"""
The **1D wave equation** describes vibrations on a string:

$$
\frac{\partial^2 u}{\partial t^2} = c^2 \cdot \frac{\partial^2 u}{\partial x^2}
$$

Where:
- \( u(x,t) \) — displacement of the wave  
- \( c \) — speed of propagation

---

### 🎼 Examples in Real Life:
- **Guitar string vibration** → standing wave
- **Tsunami wave** → traveling wave
- **Voice in tube** → wave with boundary reflections

---

### 🔬 Numerical Insight:
We simulate wave motion analytically by generating surface evolution over space \( x \) and time \( t \).  
This helps us visualize standing vs traveling wave patterns, and analyze kinetic/potential energy.
""")

# --- Sidebar ---
st.sidebar.header("🎛️ Configure Wave")
wave_type = st.sidebar.selectbox("Wave Type", ["Standing Wave", "Traveling Wave"])
amplitude = st.sidebar.slider("Amplitude (A)", 0.1, 5.0, 1.0)
wavelength = st.sidebar.slider("Wavelength (λ)", 0.5, 5.0, 2.0)
speed = st.sidebar.slider("Wave Speed (v)", 0.1, 5.0, 1.0)
duration = st.sidebar.slider("Simulation Duration (s)", 2, 10, 5)

st.sidebar.markdown("---")


# --- Simulation Grid ---
x = np.linspace(0, 10, 300)
t_vals = np.linspace(0, duration, 120)
X, T = np.meshgrid(x, t_vals)

# --- Wave Computation ---
if wave_type == "Standing Wave":
    Y = amplitude * np.sin(2 * np.pi * x / wavelength) * np.cos(2 * np.pi * speed * T / wavelength)
else:
    Y = amplitude * np.sin(2 * np.pi * (X - speed * T) / wavelength)

# --- Energy Computation ---
omega = 2 * np.pi * speed / wavelength
k = 2 * np.pi / wavelength
KE = 0.5 * (omega * amplitude * np.cos(omega * T)) ** 2
PE = 0.5 * (k * amplitude * np.sin(k * X)) ** 2
TE = KE + PE

# --- 3D Surface Plot ---
st.subheader("🌄 Wave Propagation (3D Visualization)")
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, Y, cmap="coolwarm", edgecolor='none', antialiased=True)
ax.set_xlabel("Position (x)")
ax.set_ylabel("Time (t)")
ax.set_zlabel("Displacement (u)")
ax.set_title(f"{wave_type} — 3D Dynamic Profile", fontsize=14)
st.pyplot(fig)

# --- Energy Plot ---
st.subheader("⚡ Energy Dynamics")
fig2, ax2 = plt.subplots(figsize=(9, 3.5))
ax2.plot(t_vals, KE.mean(axis=1), label="Kinetic Energy", color='#1f77b4', linewidth=2)
ax2.plot(t_vals, PE.mean(axis=1), label="Potential Energy", color='#ff7f0e', linewidth=2)
ax2.plot(t_vals, TE.mean(axis=1), label="Total Energy", color='#2ca02c', linestyle='--', linewidth=2)
ax2.set_xlabel("Time (t)")
ax2.set_ylabel("Average Energy")
ax2.set_title("Energy Distribution Over Time")
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.legend()
st.pyplot(fig2)

# Footer
st.markdown("""
---
🔗 This page is part of the **Wave Simulation Lab** — a visual learning project for physics and engineering.
""")
