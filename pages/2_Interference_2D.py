import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Wave Interference", layout="wide")

st.title("🌊 Interference of Two Waves")
st.markdown("Visualize the interference of two waves with different amplitudes, frequencies, or directions.")

# Sidebar parameters
st.sidebar.header("⚙️ Wave 1 Parameters")
A1 = st.sidebar.slider("Amplitude A₁", 0.1, 5.0, 1.0)
f1 = st.sidebar.slider("Frequency f₁ (Hz)", 0.5, 5.0, 1.0)

st.sidebar.header("⚙️ Wave 2 Parameters")
A2 = st.sidebar.slider("Amplitude A₂", 0.1, 5.0, 1.0)
f2 = st.sidebar.slider("Frequency f₂ (Hz)", 0.5, 5.0, 1.5)

speed = 1.0
duration = 3
x = np.linspace(0, 10, 300)
t = np.linspace(0, duration, 200)
X, T = np.meshgrid(x, t)

wave1 = A1 * np.sin(2 * np.pi * f1 * (T - X / speed))
wave2 = A2 * np.sin(2 * np.pi * f2 * (T + X / speed))
interference = wave1 + wave2

# Plot
st.subheader("🎥 Wave Interference (3D Plot)")

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, interference, cmap="plasma")
ax.set_xlabel("x")
ax.set_ylabel("t")
ax.set_zlabel("Amplitude")
st.pyplot(fig)

# Explanation
st.markdown("### 📚 What You See")
st.markdown("""
- This simulation shows **constructive** and **destructive interference**.
- When two waves meet **in phase**, amplitudes add → **constructive**.
- When they are **out of phase**, they cancel → **destructive**.
""")
