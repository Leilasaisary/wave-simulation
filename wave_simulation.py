import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import io
import base64

# 🌐 Page configuration
st.set_page_config(page_title="Wave Simulation", layout="wide")

# 🎨 Interface style
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        h1 {
            color: #2c3e50;
        }
        h2 {
            color: #34495e;
        }
        .stSlider > div > div {
            color: #1f77b4;
        }
    </style>
""", unsafe_allow_html=True)

# 🧾 App title
st.title("🌊 Wave Simulation on a String")

# 📘 Info block
with st.expander("📘 About this simulation"):
    st.markdown("""
    This is an interactive simulation of the **1D damped wave equation** on a stretched string.

    You can control:
    - wave speed *(c)*  
    - damping *(γ)*  
    - string length *(L)*  
    - simulation time *(T)*  
    - external sinusoidal force
    
    ---
    **Wave Equation:**

    $$
    \\frac{\\partial^2 u}{\\partial t^2} + \\gamma \\frac{\\partial u}{\\partial t} = c^2 \\frac{\\partial^2 u}{\\partial x^2} + F(x, t)
    $$

    This simulation visualizes real-time wave propagation and energy dynamics.
    """)

# 🔧 Simulation parameters
L = st.slider("🔹 String length (L)", 0.5, 5.0, 1.0)
c = st.slider("🔹 Wave speed (c)", 0.1, 5.0, 1.0)
gamma = st.slider("🔹 Damping (γ)", 0.0, 2.0, 0.1)
T = st.slider("🔹 Simulation time (seconds)", 1.0, 10.0, 3.0)
external_force = st.checkbox("🌟 Add external sinusoidal force in the middle")

# 🔢 Discretization
nx = 200
nt = 400
dx = L / (nx - 1)
dt = T / nt
x = np.linspace(0, L, nx)
r = c * dt / dx

# ⚠️ Stability check
if r >= 1:
    st.error("❌ Stability condition violated (r ≥ 1). Decrease c or T, or increase L.")
    st.stop()

# 🪄 Initial condition
u = np.zeros((nt, nx))
u[0, nx // 2] = 1.0  # initial impulse in the center
u[1, 1:-1] = u[0, 1:-1] + 0.5 * r**2 * (u[0, 2:] - 2 * u[0, 1:-1] + u[0, :-2])

# ⚡ Energy array
energy = np.zeros(nt)

# ▶️ Time evolution
for n in range(1, nt - 1):
    F = np.zeros(nx)
    if external_force:
        F[nx // 2] = np.sin(2 * np.pi * n * dt)
    u[n + 1, 1:-1] = (
        (2 - gamma * dt) * u[n, 1:-1]
        - (1 - gamma * dt) * u[n - 1, 1:-1]
        + r**2 * (u[n, 2:] - 2 * u[n, 1:-1] + u[n, :-2])
        + dt**2 * F[1:-1]
    )
    # Energy calculation
    du_dt = (u[n, :] - u[n - 1, :]) / dt
    du_dx = np.zeros_like(u[n, :])
    du_dx[1:-1] = (u[n, 2:] - u[n, :-2]) / (2 * dx)
    energy[n] = 0.5 * np.sum(du_dt**2 + c**2 * du_dx**2)

# 🎞️ Plot animation and energy side by side
col1, col2 = st.columns(2)

with col1:
    st.subheader("📉 Wave Propagation (Animated)")
    fig1, ax1 = plt.subplots()
    line1, = ax1.plot(x, u[0], color='blue')
    ax1.set_ylim(-1.2, 1.2)
    ax1.set_xlabel("x")
    ax1.set_ylabel("u(x, t)")
    ax1.grid(True)
    stframe = st.empty()
    for i in range(0, nt, 5):
        line1.set_ydata(u[i])
        ax1.set_title(f"Time t = {i * dt:.2f} s")
        stframe.pyplot(fig1)

with col2:
    st.subheader("⚡ Energy of the Wave Over Time")
    fig2, ax2 = plt.subplots()
    ax2.plot(np.arange(nt) * dt, energy, color='orange')
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Total Energy")
    ax2.grid(True)
    st.pyplot(fig2)

# 💾 CSV download
if st.button("📥 Download wave data as CSV"):
    csv_data = "\n".join([",".join(map(str, row)) for row in u])
    b64 = base64.b64encode(csv_data.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="wave_data.csv">Click here to download</a>'
    st.markdown(href, unsafe_allow_html=True)