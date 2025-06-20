import streamlit as st

# Page Configuration
st.set_page_config(page_title="📘 Wave Simulation Theory", layout="wide")

# Title
st.title("📘 Wave Simulation Lab — Theoretical Foundation")

# Introduction
st.markdown("""
Welcome to the **Wave Simulation Lab**, where mathematics meets visualization!

This lab explores **wave physics** through interactive Python simulations, applying **finite difference methods**, **Fourier analysis**, and **real audio synthesis** to model and explain complex wave behavior.
""")

# Wave Equation
st.header("🌊 The Fundamental Wave Equation")

st.latex(r"""
\frac{\partial^2 u}{\partial t^2} = c^2 \cdot \frac{\partial^2 u}{\partial x^2}
""")

st.markdown("""
This **1D wave equation** describes how displacement \( u(x,t) \) evolves over time and space:

- \( u(x,t) \) — displacement  
- \( x \) — position  
- \( t \) — time  
- \( c \) — wave speed  
""")

# Tabs Explanation
st.header("🧭 Why 8 Tabs? What Do They Represent?")

st.markdown("""
| # | Page Name           | Description |
|---|---------------------|-------------|
| 1️⃣ | **Wave 1D**            | Classical wave propagation using finite difference schemes |
| 2️⃣ | **Interference 2D**   | Superposition of two waves — visualize constructive/destructive interference |
| 3️⃣ | **Wave Energy**       | Track kinetic and potential energy evolution during simulation |
| 4️⃣ | **Fourier Transform** | Decompose complex waveforms into frequencies using FFT |
| 5️⃣ | **Wave Packet**       | Explore group velocity and dispersion from Gaussian envelopes |
| 6️⃣ | **Sound Wave**        | Simulate audio tones — generate and play real waveforms |
| 7️⃣ | **Wave Animation**    | Dynamic real-time wave visualization (animation) |
| 8️⃣ | **Virtual String**    | Interactive string instrument — pick amplitude, frequency, and play sound |
""")

st.markdown("Each one deepens your understanding of **waves in physics, music, and engineering**.")

# Numerical Methods
st.header("🔢 Numerical Methods Used")

st.subheader("🔸 Finite Difference Method (FDM)")

st.markdown("To numerically solve the wave equation, we discretize time and space:")

st.latex(r"""
u_i^{n+1} = 2(1 - r^2)u_i^n - u_i^{n-1} + r^2(u_{i+1}^n + u_{i-1}^n)
""")

st.markdown("""
Where the **Courant number** is:

""")

st.latex(r"""
r = \frac{c \cdot \Delta t}{\Delta x}
""")

st.markdown("""
✅ Explicit method — easy to implement and visualize  
""")

st.subheader("🔸 Fourier Transform")

st.markdown("""
We use the **Fast Fourier Transform (FFT)** to extract frequencies from a signal:

- Converts time-domain signals → frequency-domain  
- Reveals harmonics and spectrum  
""")

st.subheader("🔸 Wave Packet (Gaussian Envelope)")

st.markdown("Simulates a traveling packet of waves:")

st.latex(r"""
u(x,t) = A \cdot e^{-\frac{(x - vt)^2}{2\sigma^2}} \cdot \cos(kx - \omega t)
""")

st.markdown("""
- \( A \) — amplitude  
- $ \sigma $ — packet width  
- $k$, $ \omega $ — wave number and frequency  
- Shows **group velocity**, **dispersion**  
""")

# Applications
st.header("🧪 Real-World Applications")

st.markdown("""
- 🎸 Musical strings and instruments  
- 🌍 Seismic wave modeling  
- 📡 Signal processing and radio physics  
- 🔬 Engineering: bridges, beams, vibration analysis  
- 🎧 Audio synthesis and visualization  
""")

# Goals
st.header("🎯 Project Philosophy")

st.markdown("""
> **Goal**: Make complex wave physics **intuitive**, **interactive**, and **beautiful**.

Built with:
- 🐍 Python
- 📊 Matplotlib
- 🔬 NumPy
- ⚡ Streamlit

🧠 Learn waves by experimenting, not just memorizing equations!
""")

# Footer
st.markdown("---")
st.caption("👩‍💻 Developed by Leila Yerzhankyzy · 2025 · Wave Simulation Lab")